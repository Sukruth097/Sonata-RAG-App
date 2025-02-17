from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.models.vector_store import VectorStore
from src.services.storage_service import S3Storage
from src.services.llm_service import LLMService
from src.config import Config
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import tempfile
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Set environment variables
os.environ['LANGSMITH_PROJECT'] = "Sonata-RAG-Management-System"
os.environ["LANGSMITH_API_KEY"] = Config.LANGSMITH_API_KEY
os.environ["LANGSMITH_TRACING"] = "true"
os.environ['LANGSMITH_ENDPOINT'] = "https://api.smith.langchain.com"

# Initialize services
vector_store = VectorStore(Config.VECTOR_DB_PATH)
storage_service = S3Storage()
llm_service = LLMService(vector_store)

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        logger.debug("Upload endpoint called")

        if not file.filename:
            logger.warning("Empty filename")
            raise HTTPException(status_code=400, detail="No file selected")

        # Check file extension
        if not file.filename.endswith(('.txt', '.pdf')):
            logger.warning(f"Unsupported file type: {file.filename}")
            raise HTTPException(status_code=400, detail="Only .txt and .pdf files are supported")

        logger.debug(f"Processing file: {file.filename}")

        # Process the document
        try:
            text_chunks = await process_document(file)
            logger.debug(f"Document processed into {len(text_chunks)} chunks")
        except Exception as e:
            logger.error(f"Error processing document: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error processing document: {str(e)}")

        # Upload to S3
        # try:
        #     file.file.seek(0)  # Reset file pointer
        #     storage_service.upload_file(file.file, file.filename)
        #     logger.debug("File uploaded to S3")
        # except Exception as e:
        #     logger.error(f"Error uploading to S3: {str(e)}")
        #     raise HTTPException(status_code=500, detail=f"Error uploading to S3: {str(e)}")

        # Add to vector store
        try:
            vector_store.add_documents(text_chunks)
            logger.debug("Documents added to vector store")
        except Exception as e:
            logger.error(f"Error adding to vector store: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error adding to vector store: {str(e)}")

        return JSONResponse(content={
            'message': 'File uploaded and processed successfully',
            'chunks_processed': len(text_chunks)
        })

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.post("/query")
async def query(data: dict):
    if 'question' not in data:
        raise HTTPException(status_code=400, detail="No question provided")

    try:
        response = llm_service.get_response(data['question'])
        return JSONResponse(content={'response': response})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def process_document(file: UploadFile):
    """Process document based on file type and return text chunks"""
    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, file.filename)

    try:
        # Save file temporarily
        with open(temp_path, 'wb') as temp_file:
            temp_file.write(await file.read())

        # Process based on file type
        if file.filename.endswith('.pdf'):
            loader = PyPDFLoader(temp_path)
            documents = loader.load()
        elif file.filename.endswith('.txt'):
            loader = TextLoader(temp_path)
            documents = loader.load()
        else:
            raise ValueError("Unsupported file type")

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        text_chunks = text_splitter.split_documents(documents)

        return text_chunks

    finally:
        # Clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)
        os.rmdir(temp_dir)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8087)