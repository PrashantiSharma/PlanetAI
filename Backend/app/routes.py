from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from pydantic import BaseModel
from app.services import process_pdf, answer_question
from typing import Optional

api_router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    file: str 

class AnswerResponse(BaseModel):
    answer: str

@api_router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """Handles PDF file uploads."""
    try:
        file_info = process_pdf(file)
        return {"message": f"File '{file.filename}' uploaded and processed successfully!", **file_info}
    except Exception as e:
        return {"error": f"Error uploading file: {str(e)}"}



from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from langchain import OpenAI  # Or your chosen model/API

api_router = APIRouter()

@api_router.post("/ask")
async def ask_question(
    question: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    file_name = None

    # Process the uploaded file if it exists
    if file:
        try:
            file_info = process_pdf(file)
            file_name = file_info["file_name"]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

    # Handle the question
    try:
        if file_name:
            # Answer based on the processed file
            answer = answer_question(file_name, question)
        else:
            # General knowledge-based answering
            answer = get_general_answer(question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

    return {"answer": answer}


def get_general_answer(question):
    """Provide a general knowledge-based answer."""
    try:
        model = OpenAI(temperature=0)  # Replace with your configuration
        response = model(question)
        return response
    except Exception as e:
        return f"Failed to generate a general answer: {str(e)}"

