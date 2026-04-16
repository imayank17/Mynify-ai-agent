from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import sqlite3
import requests
from dotenv import load_dotenv
load_dotenv()

import os
load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY")
llm=ChatOpenAI(api_key=api_key,base_url="https://openrouter.ai/api/v1",model='openai/gpt-4o-mini')

def generate_title_llm(user_input):
    prompt = f"""
    Generate a concise 3-5 word title for the following user query.
    Do NOT include punctuation. Only return the title.

    Query: {user_input}
    """

    response = llm.invoke(prompt)
    return response.content.strip()

#----------tools-------------------

search_tool = DuckDuckGoSearchRun(region="us-en")


@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=C9PE94QUEW9VWGFM"
    r = requests.get(url)
    return r.json()



tools = [search_tool, get_stock_price]
llm_with_tools = llm.bind_tools(tools)

#--------------graph configuration----------------------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node=ToolNode(tools)

conn=sqlite3.connect(database='chatbot.db',check_same_thread=False)

#checkpoint
checkpointer=SqliteSaver(conn=conn)

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")

graph.add_conditional_edges("chat_node",tools_condition)
graph.add_edge('tools', 'chat_node')

chatbot = graph.compile(checkpointer=checkpointer)

# no of threads
def retrieve_all_threads():
    all_threads=set()
    for checkpoint in checkpointer.list(None):
       all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)