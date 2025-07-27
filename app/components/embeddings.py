from langchain_huggingface import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def get_embeddings():
    try:
        logger.info("Initializing HuggingFace embeddings")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}  # tránh lỗi GPU
        )
        logger.info("HuggingFace embeddings initialized successfully")
        return embeddings
    except Exception as e:
        logger.error(f"Error initializing HuggingFace embeddings: {e}")
        raise CustomException(f"Failed to initialize embeddings: {e}")