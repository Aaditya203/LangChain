from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

loader = TextLoader('E:/LangChain/RAG/DocumentLoaders/edtech_company_policy_rules.txt',encoding='utf-8')

docs = loader.load()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Generate a summary of this document : {document}",
    input_variables=['document']
    )

chain  = prompt | model | parser

result = chain.invoke({'document':docs[0].page_content})
print(result)