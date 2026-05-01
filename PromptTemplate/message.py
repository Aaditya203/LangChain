from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
history = [
    SystemMessage(content='You are a good project developer whos task is to think a good industry level project')
]

while True:
    user_input = input("You: ")
    history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    response = model.invoke(history)
    history.append(AIMessage(content=response.content))
    print(response.content)

print(history)