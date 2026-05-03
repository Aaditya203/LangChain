from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableBranch,RunnableLambda
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment of the feedback as negative or positive")

parser = PydanticOutputParser(pydantic_object=Feedback)


prompt = PromptTemplate(
    template="Classify the sentiment of the follwing feedback into positive or negative {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

classifier_chain = prompt | model | parser


prompt2 = PromptTemplate(
    template='Write an appropriate single 2 line response for the positive feedback {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate single 2 line response for the negative feedback {feedback}',
    input_variables=['feedback']
)
parser2 = StrOutputParser()
final_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive',prompt2 | model | parser2),
    (lambda x:x.sentiment == 'negative',prompt3 | model | parser2),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chains = classifier_chain | final_chain

result = chains.invoke({'feedback':'The phone is awesome'})
print(result)