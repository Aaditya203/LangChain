from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()
# Use the updated model name
embedding = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

splitter = SemanticChunker(
    embedding,breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

text = """
Artificial Intelligence is transforming industries.
Machine learning models are becoming more powerful.

Football is one of the most popular sports in the world.
Millions of people watch international tournaments.
"""

docs = splitter.create_documents([text])
print(docs[0].page_content)