import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("ishowfinance")

#dictionary of predetermined responses, I tried to think of ones that would be commonly asked, as well as throwing in some hard coded easter eggs.
responses = {  
    "hello": "Hello! How can I assist you?",
    "hi": "Hi there!",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Goodbye! Have a good day!",
    "how are you?": "I'm here to help you with your finance questions!",
    "what is a budget?": "A budget is a fun plan for your income and expenses.",
    "can you show me finance?": "Always.",
    "what else can you do?": "I am programed to answer questions exclusievly about finance.",
}

#loops the program, so mulitpule questions dont have to restart it
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask ishowfinance a question here......")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Makes user input more readable to groq
    cleaned_input = user_input.strip()
    
    if cleaned_input in responses:
        response = responses[cleaned_input]
    else:
        try:
            completion = client.chat.completions.create(
                model="openai/gpt-oss-20b",
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
            response = completion.choices[0].message.content
        except: response = f"An error occurred: {e}"

    #displays the response, thank you documentation.
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
