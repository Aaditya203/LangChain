from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough,RunnableParallel,RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=['topic']
)
parser = StrOutputParser()

chain = prompt | model | parser

prompt2 = PromptTemplate(
    template="Explain the given joke: {joke}",
    input_variables=['joke']
)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2,model,parser)
})

final_chain = chain | parallel_chain

print(final_chain.invoke({'topic':'BGMI'}))