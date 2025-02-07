from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Define the URL to scrape data from
urls = ["https://brainlox.com/courses/category/technical"]

# Function to load data from URL
def load_url_data(urls):
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()
    return documents

documents = load_url_data(urls)

# Function to create chunks of text
def create_chunks(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

text_chunks = create_chunks(extracted_data=documents)

# Function to initialize embedding model
def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

embedding_model = get_embedding_model()

# Define FAISS vector storage path
DB_FAISS_PATH = "vector_store/db_emb"

# Store the embeddings in FAISS
db = FAISS.from_documents(text_chunks, embedding_model)
db.save_local(DB_FAISS_PATH)
