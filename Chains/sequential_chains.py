from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Generate a 5 pointer important summary on {text}",
    input_variables=['text']
)

chains = prompt1 | model | parser | prompt2 | model | parser

result = chains.invoke({'topic':'DSA'})
print(result)