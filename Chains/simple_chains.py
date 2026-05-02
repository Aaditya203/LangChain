from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

template = PromptTemplate(
    template="Generate 5 facts about {topic}",
    input_variables=['topic']
)


chain = template | model | parser

result = chain.invoke({'topic':'BGMI'})
print(result)