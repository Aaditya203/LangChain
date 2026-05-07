from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

loader = WebBaseLoader(web_path="https://www.amazon.in/iPhone-Pro-256-Promotion-Breakthrough/dp/B0FQG9FPFJ?th=1")

docs = loader.load()

prompt = PromptTemplate(
    template = "You have to give answer to the question with context given , question:{question} , context: {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'question':'Whats the prize of the phone','text':docs[0].page_content})
print(result)
