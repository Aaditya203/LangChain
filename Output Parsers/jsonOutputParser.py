from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
parser = JsonOutputParser()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
template = PromptTemplate(
    template="Give me the name age and city of a famous cricketer \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
prompt = template.format()

response = model.invoke(prompt)
final_result = parser.parse(response.content)
print(final_result)