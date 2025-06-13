from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# Chat Template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support assistant'), 
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}'),
    MessagesPlaceholder(variable_name="chat_history")
])
chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)

#Create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'What is the return policy?'})
print(prompt)
                              