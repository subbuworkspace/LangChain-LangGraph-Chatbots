# 🤖 LangChain & LangGraph Chatbots

A practical Generative AI project demonstrating how to build **Single Chatbot and Multi-Chatbot workflows** using **LangChain and LangGraph**.

The project starts with a simple chatbot and then extends the concept into a graph-based multi-chatbot architecture where different chatbot nodes can handle different responsibilities.

---

## 🚀 Project Overview

This repository covers two implementations:

### 1️⃣ Single Chatbot

A basic LLM chatbot built using **LangChain**.

```text
User
 ↓
LangChain
 ↓
LLM
 ↓
AI Response
```

### 2️⃣ Multi-Chatbot

A graph-based chatbot workflow built using **LangGraph**.

```text
                    ┌── Chatbot 1 ──┐
User Message → Router               → Final Response
                    └── Chatbot 2 ──┘
```

The idea is to divide responsibilities between different chatbot nodes instead of depending on one chatbot for everything.

---

# 🧠 Technologies Used

- Python
- LangChain
- LangGraph
- Groq / LLM
- TypedDict
- StateGraph
- Environment Variables

---

# 📁 Project Structure

```text
LangChain-LangGraph-Chatbots/
│
├── single_chatbot/
│   └── single_chatbot.py
│
├── multi_chatbot/
│   └── multi_chatbot.py
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── LICENSE
```

---

# 1️⃣ Single Chatbot

The Single Chatbot demonstrates the basic interaction between a user and an LLM.

### Workflow

```text
User Input
    ↓
LangChain
    ↓
LLM
    ↓
Response
```

### Main Concept

The chatbot receives a user message and sends it to the LLM through LangChain.

```python
response = llm.invoke(user_message)
```

### Example

```text
User: What is Generative AI?

AI: Generative AI refers to AI systems that can create
new content such as text, images, audio and code.
```

---

# 2️⃣ Multi-Chatbot with LangGraph

The Multi-Chatbot demonstrates how a problem can be divided between different chatbot nodes.

Instead of:

```text
User → One Chatbot → Response
```

we can create:

```text
User
 ↓
LangGraph
 ↓
Chatbot Node 1
 ↓
Chatbot Node 2
 ↓
Final Response
```

Each node can have a specific responsibility.

For example:

```text
          User
           ↓
       LangGraph
        /      \
       ↓        ↓
  Research   Technical
  Chatbot     Chatbot
       \        /
        ↓      ↓
       Final Response
```

---

# 🔄 LangGraph Workflow

LangGraph represents the application as a graph.

### State

The state contains information shared between chatbot nodes.

```python
class State(TypedDict):
    messages: list
```

### Nodes

Each chatbot can be represented as a node.

```python
builder.add_node("chatbot_1", chatbot_1)
builder.add_node("chatbot_2", chatbot_2)
```

### Edges

Edges define how the workflow moves between nodes.

```python
builder.add_edge(START, "chatbot_1")
builder.add_edge("chatbot_1", "chatbot_2")
builder.add_edge("chatbot_2", END)
```

---

# 🆚 Single Chatbot vs Multi-Chatbot

| Feature | Single Chatbot | Multi-Chatbot |
|---|---|---|
| Framework | LangChain | LangGraph + LangChain |
| Architecture | Linear | Graph-based |
| LLM Nodes | One | Multiple |
| State | Simple | Shared State |
| Routing | Limited | Possible |
| Specialization | Low | High |
| Workflow | Simple | Flexible |
| Agentic AI | Basic | Foundation for Agentic AI |

---

# 🔑 LangChain vs LangGraph

## LangChain

LangChain helps connect applications with:

- LLMs
- Prompts
- Tools
- Retrievers
- Memory
- Agents
- Chains

Basic architecture:

```text
Application
     ↓
LangChain
     ↓
LLM
```

---

## LangGraph

LangGraph is useful when the application requires a more structured workflow.

```text
          ┌── Node 1 ──┐
START →   │            │
          └── Node 2 ──┘
                 ↓
                END
```

It provides concepts such as:

- State
- Nodes
- Edges
- Conditional routing
- Loops
- Multiple agents
- Human-in-the-loop workflows

---

# 💡 Why Use Multiple Chatbots?

A single chatbot may handle everything, but specialized chatbots can divide responsibilities.

For example:

```text
Customer Question
       ↓
     Router
       ↓
 ┌─────┼──────────┐
 ↓     ↓          ↓
Sales Technical Support
Bot      Bot       Bot
 └─────┬──────────┘
       ↓
Final Response
```

This approach can make larger AI applications easier to organize and extend.

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/LangChain-LangGraph-Chatbots.git
```

```bash
cd LangChain-LangGraph-Chatbots
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 API Key

Create an environment variable for your LLM API key.

Example:

```text
GROQ_API_KEY=your_api_key_here
```

Never upload the real API key to GitHub.

Use:

```text
.env
```

and keep it inside `.gitignore`.

---

# ▶️ Run Single Chatbot

```bash
python single_chatbot/single_chatbot.py
```

---

# ▶️ Run Multi-Chatbot

```bash
python multi_chatbot/multi_chatbot.py
```

---

# 📚 Important Concepts Learned

This project helped me understand the progression:

```text
Python
   ↓
LLM
   ↓
LangChain
   ↓
Chains
   ↓
LangGraph
   ↓
State
   ↓
Nodes
   ↓
Edges
   ↓
Multiple Chatbots
   ↓
Agentic AI
```

---

# 🎯 Interview Questions

### 1. What is LangChain?

LangChain is a framework for developing applications powered by large language models.

### 2. What is LangGraph?

LangGraph is used to build stateful, graph-based AI workflows.

### 3. What is a node in LangGraph?

A node represents a function or processing step in the workflow.

### 4. What is an edge?

An edge defines how the workflow moves from one node to another.

### 5. What is State?

State contains information shared between different nodes in the graph.

### 6. What is the difference between LangChain and LangGraph?

LangChain provides components for building LLM applications, while LangGraph provides a graph-based architecture for building more complex, stateful workflows.

### 7. Why use multiple chatbots?

Multiple chatbots can specialize in different tasks, making the overall AI workflow easier to organize and extend.

### 8. What is Agentic AI?

Agentic AI refers to AI systems that can perform tasks through reasoning, decisions, tools, workflows and interactions with their environment.

---

# 🚀 Future Improvements

The project can be extended with:

- Conditional routing
- Tool calling
- RAG
- Vector databases
- Conversation memory
- Web search
- Human-in-the-loop
- Multiple specialized agents
- Streamlit frontend
- Gradio frontend
- Database integration
- Multi-agent collaboration

Future architecture:

```text
                    ┌── Research Agent ──┐
                    │                    │
User → Router ──────┼── Technical Agent ─┼── Final Response
                    │                    │
                    └── Support Agent ───┘
```

---

# 📌 Key Takeaway

This project demonstrates the evolution from a **simple LLM chatbot to a structured multi-chatbot workflow**.

```text
Single Chatbot
      ↓
LangChain
      ↓
LangGraph
      ↓
Multiple Chatbots
      ↓
Specialized Agents
      ↓
Agentic AI
```

It provides a practical foundation for building more advanced **Generative AI and Agentic AI applications**.

---

# 👨‍💻 Author

**Subrata Mondal**

Data Analyst | Python | SQL | Power BI | Machine Learning | Generative AI | Agentic AI

⭐ If you find this project useful, consider starring the repository.
