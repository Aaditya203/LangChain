from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough, RunnableLambda,RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Generate a joke on {topic}",
    input_variables=['topic']
)
def count(word):
    return len(word.split())


chain = prompt | model | parser

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'count':RunnableLambda(count)
})
final_chain = chain | parallel_chain

print(final_chain.invoke({'topic':'Congress leader Rahul'}))