import os 
import openai

def chatgpt():

    messages = [
	{"role": "system", "content": "You will be given a book text and then user will answer questions about the book"}
]

    open.api_key = os.getenv("OPENAI_API_KEY")

    while True:
        content = input("User: ")
        
        messages.append({"role":"user", "content":content})
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages
            )
        
        chat_response = completion.choices[0].message.content
        print(f"ChatGPT: {chat_response}")
        messages.append({"role":"assistant", "content":chat_response})
