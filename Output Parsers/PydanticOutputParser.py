from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Person(BaseModel):
    name: str = Field(description="Name of The Person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="City of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Genrate the name , age and city of a fictional person from {country} \n {format_instruction}",
    input_variables=['country'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'country':'indian'})

print(result)