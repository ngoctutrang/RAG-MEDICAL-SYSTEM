from langchain_community.vectorstores import FAISS

from app.components.embeddings import get_embeddings

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config import DB_FAISS_PATH

import os

logger = get_logger(__name__)

def load_vector_store():
    try:
        logger.info("Loading FAISS vector store")
        embeddings = get_embeddings()

        if os.path.exists(DB_FAISS_PATH):
            logger.info(f"FAISS vector store found at {DB_FAISS_PATH}")
            
            return FAISS.load_local(
                DB_FAISS_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            logger.warning(f"FAISS vector store not found at {DB_FAISS_PATH}. Returning None.")
            return None
    except Exception as e:
        logger.error(f"Error loading FAISS vector store: {e}")

def save_vector_store(documents):
    try:
        if not documents:
            logger.warning("No documents provided to create vector store.")
            raise CustomException("No documents to create vector store.")
        logger.info("Creating FAISS vector store")
        embeddings = get_embeddings()
        db = FAISS.from_documents(
            documents,
            embeddings
        )
        db.save_local(DB_FAISS_PATH)
        logger.info(f"FAISS vector store saved to {DB_FAISS_PATH}")
        return db
    except Exception as e:
        logger.error(f"Error saving FAISS vector store: {e}")
        raise CustomException(f"Failed to save vector store: {e}")