from dotenv import load_dotenv
import os
from src.helper import filter_to_minimal_docs, load_pdf_file, split_text, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
 

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

extracted_data = load_pdf_file(data = 'data/')
minimal_docs = filter_to_minimal_docs(extracted_data)
text_chunks = split_text(minimal_docs)
embeddings = download_hugging_face_embeddings()


pc = Pinecone(api_key = PINECONE_API_KEY)

index_name = "medibot-index"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension = 384, 
        metric = "cosine",
        spec = ServerlessSpec(cloud = "aws", region = "us-east-1")
    )

index = pc.Index(index_name)


docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    embedding = embeddings,
    index_name = index_name
)