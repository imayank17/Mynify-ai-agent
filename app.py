import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage



CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]


#loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

 # take the user text       
user_input=st.chat_input("type here...")

if user_input:
    #first add the message in the message history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message("user"):
        st.text(user_input)

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]},config=CONFIG)
    ai_message=response['messages'][-1].content
    # add the message in the message history
    st.session_state['message_history'].append({'role':'Assistant','content':ai_message})
    with st.chat_message("Assistant"):
        st.text(ai_message)
 



