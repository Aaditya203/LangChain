from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

response = model.invoke("Whats the capital of india?")

print(response.content)