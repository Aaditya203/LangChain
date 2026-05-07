from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('E:/LangChain/RAG/DocumentLoaders/book.pdf')

docs = loader.load()

print(docs[0].page_content)