# 🤖 LangChain AI Agents

A Python-based learning project focused on exploring **LangChain, AI Agents, LLMs, and Tool Calling** to understand how intelligent applications can interpret user instructions, interact with external tools, and perform tasks autonomously.

This repository contains practical experiments and implementations designed to build a strong foundation in AI agent development and LLM-powered applications.

## 🚀 Project Objectives

- Understand the fundamentals of Large Language Models (LLMs).
- Learn how to build AI-powered applications using LangChain.
- Explore AI Agents and their working mechanisms.
- Understand tool integration and function calling.
- Learn how AI agents process user instructions and select appropriate actions.
- Develop practical experience with Python-based Generative AI applications.

## 🛠️ Technologies & Tools

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Framework for building LLM applications |
| OpenAI API | Access to language models |
| JSON | Structured data and tool arguments |
| VS Code | Development environment |

## 📂 Project Structure

```text
Langchain_AI_Agents/
│
├── codes/
│   ├── basics/
│   │
│   ├── agents/
│   │
│   └── tools/
│
├── README.md
└── requirements.txt
```

*Note: The folder structure above is a suggested organization. Adjust it to match the actual repository.*

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rudranil2004-Das/Langchain_AI_Agents.git
```

### 2. Navigate to the Project Directory

```bash
cd Langchain_AI_Agents
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If a requirements file is not available yet, install the required packages individually based on the scripts:

```bash
pip install langchain langchain-openai openai python-dotenv
```

### 6. Configure API Keys

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

Never share your API key or commit your `.env` file to GitHub.

## 🧠 Key Concepts

### 1. Large Language Models (LLMs)

Understanding how language models process natural-language instructions and generate responses.

### 2. LangChain

Exploring the LangChain framework and its components for connecting language models with application logic.

### 3. AI Agents

Understanding how AI agents interpret instructions, decide which actions are necessary, and interact with available tools.

### 4. Tool Calling

Learning how language models can request the execution of external Python functions to perform tasks.

### 5. Agent Workflow

```text
       User Input
           |
           v
      AI Language Model
           |
           v
     Analyze the Request
           |
           v
      Select an Action
           |
           v
      Execute Tool
           |
           v
      Get Tool Result
           |
           v
      Final AI Response
```

## 💻 Development Environment

- Operating System: Windows
- Programming Language: Python
- IDE: Visual Studio Code
- Environment: Python Virtual Environment

## 🔮 Future Improvements

- Implement more advanced AI agents.
- Integrate additional external tools and APIs.
- Explore Retrieval-Augmented Generation (RAG).
- Implement conversational memory.
- Build multi-agent systems.
- Develop real-world AI automation applications.
- Create interactive interfaces for AI agents.

## 🎯 Learning Outcomes

Through this project, I aim to gain practical experience in:

- Generative AI development.
- LLM integration.
- LangChain architecture.
- AI agent workflows.
- Function and tool calling.
- Python-based AI automation.

## 👨‍💻 Author

**Rudranil Das**

- GitHub: [Rudranil2004-Das](https://github.com/Rudranil2004-Das)
- Portfolio: [Personal Portfolio](https://portfolio-jhlp.vercel.app/)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/rudranil-das-34783725b)

---

⭐ If you find this repository useful, feel free to explore and star it!

**Building, Learning, and Exploring the World of Generative AI.**
