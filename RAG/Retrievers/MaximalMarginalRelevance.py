from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
embedding = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]
vectorStores = FAISS.from_documents(
    embedding=embedding,
    documents=docs
)

retriever = vectorStores.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"lambda_mult":1}
)

result = retriever.invoke("What is Langchain?")

for i,doc in enumerate(result):
    print(f"Result: {i+1}")
    print(f"Content: {doc.page_content}")