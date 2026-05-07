from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = "E:/LangChain/RAG/DocumentLoaders/Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
docs = loader.load()

print(docs[2].page_content)