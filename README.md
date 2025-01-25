# PlanetAI
 This project provides a question answering system that allows users to upload a PDF file, extract the text, and then ask questions related to the contents of that PDF. It uses OpenAI’s API via LangChain for natural language processing and querying.


## Features
- Upload a PDF file.
- Extract text from the PDF file.
- Ask questions based on the content of the uploaded PDF.
- Provides answers by using LangChain and OpenAI’s GPT model.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Create a `.env` File
In the root directory of the project, create a file named `.env` and add your OpenAI API key as follows:

```bash
OPENAI_API_KEY=your_api_key_here
```

You can get your OpenAI API key from [OpenAI’s website](https://beta.openai.com/signup/).

### 3. Install Dependencies
Create a virtual environment and install the necessary dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows
.\venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Running the Application
Once everything is set up, you can run the FastAPI application:

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

### 5. Endpoints
- **POST /ask**
  - This endpoint allows users to submit a question along with a PDF file.
  - **Parameters:**
    - `question` (string): The question to ask.
    - `file` (file): The PDF file to process.

### 6. Important Notes
- Make sure you have a valid OpenAI API key set up in the `.env` file.
- This application requires the `python-dotenv` package to load environment variables from the `.env` file.

### 7. .gitignore
To ensure your `.env` file does not get committed to version control, make sure the following line is in your `.gitignore` file:

```bash
.env
```

### 8. Troubleshooting
If you encounter any issues such as missing environment variables or API key errors, make sure:
- Your `.env` file is correctly placed in the root directory.
- The API key is set correctly.
- Dependencies are installed via `pip install -r requirements.txt`.

### 9. Deployment
For cloud deployment (Heroku, AWS, etc.), follow their documentation for setting environment variables securely. You can use the `.env` file locally, but on the cloud, you’ll need to configure the OpenAI API key through their environment variable settings.

---

## License

This project is licensed under the MIT License.

---
