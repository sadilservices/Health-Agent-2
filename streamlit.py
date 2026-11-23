import os
import streamlit as st
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import requests
import os

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature=0.0,
    max_retries=2,
    api_key=GROQ_API_KEY
)


def diagnose_health(symptoms:  str) -> str:
    """Diagnose the health by analyzing the symptoms"""

    res = requests.get(f'https://medlineplus.gov/medlineplus-connect/web-service/')
    data = res.json
    return data

def get_symptoms () -> str:
    """Get the AI agent name."""
    return "Health Agent"


agent = create_agent(
    model = llm,
    tools=[diagnose_health, get_symptoms],
    system_prompt=f"You are a health agent."
)

user_input = input("Describe your symptoms: ") 

response=agent.invoke(
    {"messages" : [{"role": "user", "content": user_input}]}
    )


load_dotenv ()
api_key=os.getenv('GEMINI_API_KEY')


client = genai.Client(api_key=api_key)


st.title("Talk to Chatbot")
st.write("This app demonstrate a conversational agent.")

user_input=st.text_input("Ask a question")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model='gemini-3.8-flash', contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
                )
        )
        
        st.write(response.text)