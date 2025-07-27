import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


HF_TOKEN = os.environ.get("HF_TOKEN", "")

HUGGINGFACE_REPO_ID ="mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH = "vector_store/db_faiss"
DATA_PATH = "data/"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50