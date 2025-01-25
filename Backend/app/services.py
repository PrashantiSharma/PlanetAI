import os
from langchain import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from app.storage import save_file, save_extracted_text, get_extracted_text
from app.utils import extract_text_from_pdf
from dotenv import load_dotenv


def process_pdf(file):
    file_path = save_file(file)
    extracted_text = extract_text_from_pdf(file_path)
    save_extracted_text(file.filename, extracted_text)
    return {"file_name": file.filename, "size": len(extracted_text)}

def answer_question(file_name, question):
    # Ensure API key is set
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set. Please set it as an environment variable.")

    text = get_extracted_text(file_name)
    if not text:
        raise ValueError(f"File '{file_name}' not found or text not extracted.")

    # Split the text into chunks for embedding and search
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    print(f"Text split into {len(chunks)} chunks.")

    # Create the OpenAIEmbeddings instance with API key
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vector_store = FAISS.from_texts(chunks, embeddings)
    print(f"Vector store created with {len(chunks)} entries.")

    # Perform similarity search on the vector store
    docs = vector_store.similarity_search(question, k=3)
    print(f"Similarity search returned {len(docs)} documents.")

    # Load the QA chain and pass the API key for OpenAI
    chain = load_qa_chain(OpenAI(temperature=0, openai_api_key=api_key), chain_type="stuff")
    answer = chain.run(input_documents=docs, question=question)
    return answer
