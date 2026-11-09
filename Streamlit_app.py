from groq import Groq
from getpass import getpass
import os

client = Groq(api_key=getpass("Groq API key: "))

responses = {
    "hello": "Hello! How can I assist you?",
    "hi": "Hi there!",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Goodbye! Have a good day!",
    "how are you?": "I'm here to help you with your finance questions!",
    "what is a budget?": "A budget is a plan for your income and expenses.",
}

def chatbot_response(user_input):
    cleaned_input = user_input.lower().strip()
    
    # This Checks dictionary first, making sure there is a predisposed response it can give
    if cleaned_input in responses:
        return responses[cleaned_input]
    
    # Fallback to Groq API, if not in dictionary or for a more refined response.streamlit run app.py
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful finance chatbot. Answer questions related to personal finance, banking, and budgeting."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

name = input("Please enter your name: ")
print(f"ChatBot: Hello {name}! Ask me anything.")
print("Type 'exit' to end the conversation.")

while True:
    user_input = input(f"{name}: ")

    if user_input.lower().strip() == "exit":
        print("ChatBot: Goodbye! Have a great day!")
        break

    response = chatbot_response(user_input)
    print(f"ChatBot: {response}")