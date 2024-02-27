import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser
import os
from os import getenv

# api_key = os.getenv("OPENAI_API_KEY")

chatllm = ChatOpenAI(temperature=0.6, model= 'gpt-3.5-turbo', )
    
template = "You are a Medical Consultant AI assistant. When ever the user gives any input, you should give the user suggestion on how he can perform a temporary first aid or any temporary action he can take based on the emergency he has mentione in the text untill the actual emergency services arrive to assist him and then give the answer. The answer should be comma seperated and should be given as a paragraph or pointwise according to the query given. Beging the answer by mentioning 'The concerned departments are at work to well assist you. Meanwhile you can'"
human_template = "{text}"
chatprompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template)
])
chain = chatprompt|chatllm

def main():
    st.image("/Users/karthiksagar/VTAPP HACKATHON/VcareIT.png", width=70)
    st.title('VcareIt')

    # Name
    name = st.text_input('Name')

    # Registration number
    reg_number = st.text_input('Registration Number')

    # Blood group
    blood_group = st.text_input('Blood Group')

    # Email ID
    email_id = st.text_input('Email ID')

    # Emergency issue
    emergency_issue = st.text_area('Emergency Issue', height=100)

    # Submit button
    submitted = st.button('Submit Request')

    if submitted:
        # Send request to concerned parties
        # Placeholder for actual logic to send request
        st.success('Form submitted successfully!')
        st.info('Your request has been sent to the concerned parties.')
        temp_messege = chain.invoke({"text":emergency_issue})
        st.info(temp_messege.content)


if __name__ == '__main__':
    main()
