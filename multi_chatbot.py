import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langgraph.graph import StateGraph, START, END


# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")


# --------------------------------------------------
# Create LLM
# --------------------------------------------------

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant",
    temperature=0.7
)


# --------------------------------------------------
# Define Graph State
# --------------------------------------------------

class State(TypedDict):
    user_input: str
    chatbot_1_response: str
    chatbot_2_response: str
    final_response: str


# --------------------------------------------------
# Chatbot 1 - Analyst
# --------------------------------------------------

def chatbot_1(state: State):

    prompt = f"""
    You are Chatbot 1, an analytical assistant.

    Analyze the user's question and provide
    useful points or reasoning.

    User Question:
    {state["user_input"]}
    """

    response = llm.invoke(prompt)

    return {
        "chatbot_1_response": response.content
    }


# --------------------------------------------------
# Chatbot 2 - Reviewer
# --------------------------------------------------

def chatbot_2(state: State):

    prompt = f"""
    You are Chatbot 2, a reviewer.

    Review the following analysis and improve it.
    Give a clear and practical response.

    User Question:
    {state["user_input"]}

    Chatbot 1 Analysis:
    {state["chatbot_1_response"]}
    """

    response = llm.invoke(prompt)

    return {
        "chatbot_2_response": response.content
    }


# --------------------------------------------------
# Final Response
# --------------------------------------------------

def final_response(state: State):

    prompt = f"""
    Create the final answer for the user.

    User Question:
    {state["user_input"]}

    Analyst Response:
    {state["chatbot_1_response"]}

    Reviewer Response:
    {state["chatbot_2_response"]}

    Combine the useful information into one
    clear and concise answer.
    """

    response = llm.invoke(prompt)

    return {
        "final_response": response.content
    }


# --------------------------------------------------
# Create LangGraph
# --------------------------------------------------

graph = StateGraph(State)

# Add nodes
graph.add_node("chatbot_1", chatbot_1)
graph.add_node("chatbot_2", chatbot_2)
graph.add_node("final_response", final_response)

# Add edges
graph.add_edge(START, "chatbot_1")
graph.add_edge("chatbot_1", "chatbot_2")
graph.add_edge("chatbot_2", "final_response")
graph.add_edge("final_response", END)

# Compile graph
app = graph.compile()


# --------------------------------------------------
# Run Multi-Chatbot
# --------------------------------------------------

print("Multi-Chatbot LangGraph Started")
print("Type 'exit' to stop.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    result = app.invoke({
        "user_input": user_input,
        "chatbot_1_response": "",
        "chatbot_2_response": "",
        "final_response": ""
    })

    print("\nChatbot 1 - Analysis:")
    print(result["chatbot_1_response"])

    print("\nChatbot 2 - Review:")
    print(result["chatbot_2_response"])

    print("\nFinal Answer:")
    print(result["final_response"])

    print("\n" + "-" * 60 + "\n")
