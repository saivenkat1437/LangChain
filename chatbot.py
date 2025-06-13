from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()   
model = ChatOpenAI()
Chat_history = []
while True:
    user_input = input("You: ")
    Chat_history.append(user_input)
    if user_input.lower() == 'exit':
        break
    result = model.invoke(user_input)
    Chat_history.append(result.content)
    print(f"AI: {result.content}") 
print(Chat_history)