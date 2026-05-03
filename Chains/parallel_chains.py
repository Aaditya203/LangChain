from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a short detailed notes about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a quiz consisting of 5 questions and 2 options on {topic}",
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} quiz -> {quiz}",
    input_variables=['notes','quiz']
)

runnable_parallel = RunnableParallel({
    'notes':prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

chain = prompt3 | model | parser

final_chain = runnable_parallel | chain

print(final_chain.invoke({'topic':'Python'}))