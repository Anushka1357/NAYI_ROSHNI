import streamlit as st
import pandas as pd
import openai

# Set up OpenAI API key (You need to sign up for OpenAI API and get your API key)
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

# Define a function to interact with GPT-based chatbot
def ask_chatbot(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use 'gpt-4' or 'gpt-3.5-turbo' model
            messages=[{"role": "user", "content": question}],
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Define function to analyze resume and suggest jobs
def analyze_resume(file):
    # Here, you would implement the logic to analyze the resume
    # For simplicity, we assume any resume gets these jobs:
    job_suggestions = ["Software Engineer", "Data Analyst", "Project Manager"]
    return job_suggestions

# Streamlit Web Application
st.title("Welcome to the Generative AI Job Advisor")

# Section 1: Resume Upload and Job Suggestions
st.header("Upload Your Resume for Job Suggestions")
uploaded_file = st.file_uploader("Choose your resume file", type=['pdf', 'docx'])

if uploaded_file is not None:
    # Simulate job suggestion based on resume
    st.success("Resume uploaded successfully.")
    job_suggestions = analyze_resume(uploaded_file)
    st.subheader("Job Suggestions for You")
    for job in job_suggestions:
        st.write(f"- {job}")

# Section 2: Chat with the Generative AI Chatbot
st.header("Chat with the AI Assistant")
user_input = st.text_input("Ask me anything!")

if st.button("Send"):
    if user_input:
        chatbot_response = ask_chatbot(user_input)
        st.subheader("AI Response")
        st.write(chatbot_response)
    else:
        st.error("Please enter a question to ask the chatbot.")

