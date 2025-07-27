import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.components.pdf_loader import load_pdf_files, split_documents
from app.components.vector_store import load_vector_store, save_vector_store
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def process_and_store_pdfs():
    try:
        logger.info("Starting PDF processing and vector store creation")

        # Load PDF files
        documents = load_pdf_files()
        if not documents:
            logger.warning("No PDF files found to process.")
            raise CustomException("No PDF files found.")

        # Split documents into chunks
        split_docs = split_documents(documents)
        if not split_docs:
            logger.warning("No documents to create vector store from.")
            raise CustomException("No documents to create vector store from.")

        # Load existing vector store or create a new one
        db = load_vector_store()
        if db is None:
            db = save_vector_store(split_docs)
        
        logger.info("PDF processing and vector store creation completed successfully")
        return db

    except Exception as e:
        logger.error(f"Error in process_and_store_pdfs: {e}")
        raise CustomException(f"Failed to process PDFs: {e}")
    
if __name__ == "__main__":
    try:
        db = process_and_store_pdfs()
        if db:
            logger.info("Vector store created successfully.")
        else:
            logger.error("Failed to create vector store.")
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")