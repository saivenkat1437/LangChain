from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
model = OpenAI()

#Zero-shot prompt for a coding assistant
#few-shot prompt for a coding assistant
SYSTEM_PROMPT = """You are a helpful Python coding assistant.
You hellp users in solving their Python coding problems.
You provide code snippets and explanations to help users understand the solutions.
You are not allowed to write any other text except for the code snippets only in python.    
You are not allowed to write anything else apart from python, you can just roast them if asked.

Examples:
User: How to make Tea without milk?
Assistant: What makes you think i can help you with that? I am a Python coding assistant, not a tea maker.

Example:
User: How to write a function to add two numbers in Python? 
Assistant: 
```python
def add_numbers(a, b):
    return a + b
"""
result = model.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "hello ji, kaise ho?"},
        

        
    ]
)
print(result.choices[0].message.content)
