import os

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders.pdf import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException(f"Data path {DATA_PATH} does not exist.")
        
        logger.info(f"Loading PDF files from {DATA_PATH}")

        loader = DirectoryLoader(
            DATA_PATH,
            glob="**/*.pdf",
            loader_cls=PyMuPDFLoader
        )
        documents = loader.load()

        if not documents:
            logger.warning("No PDF files found in the specified directory.")
        else:
            logger.info(f"Loaded {len(documents)} PDF files.")
        return documents
    except Exception as e:
        logger.error(f"Error loading PDF files: {e}")
        return []

def split_documents(documents):
    try:
        if not documents:
            logger.warning("No documents to split.")
            raise CustomException("No documents to split.")
        
        logger.info("Splitting documents into chunks")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        split_docs = text_splitter.split_documents(documents)
        logger.info(f"Split documents into {len(split_docs)} chunks.")
        return split_docs
    except Exception as e:
        logger.error(f"Error splitting documents: {e}")
        return []
