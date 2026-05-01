from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

template = ChatPromptTemplate([
    ('system','You are a Helpful customer support assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])
chat_history = []
with open('chat_history.txt') as fs:
    chat_history.append(fs.readline())

prompt = template.invoke({'chat_history':chat_history,'query':'Where is my refund'})

print(prompt)
