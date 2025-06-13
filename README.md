# 🧠 LangChain – Building LLM-Powered Apps

Welcome to a crash course on **LangChain**, the go-to Python framework for building applications powered by **Large Language Models (LLMs)**. Whether you're crafting chatbots, data agents, or knowledge assistants, LangChain provides a modular approach to work with **prompts**, **memory**, **indexes**, **chains**, and more.

---

## 🚀 What You'll Learn

- ✅ What is LangChain?
- 🔠 How Prompt Templates Work
- 🧩 Types of Prompts (Zero-shot, Few-shot, Chat)
- 🧠 Working with Memory for Conversations
- 🔗 Chains: From Input → Output Workflows
- 🗃️ Vector Indexes & Embeddings
- 🤖 Building Agents with Tools
- 📚 Putting it All Together

---

## 📘 What is LangChain?

LangChain is a powerful **Python/JS library** that helps developers **orchestrate components** required for building **LLM-powered applications**. Think of it as the glue between LLMs (like OpenAI, Cohere) and tools like vector databases, APIs, files, or memory.

---

## 🔠 Prompt Engineering in LangChain

Prompts are instructions or templates that guide LLMs. LangChain helps structure prompts using dedicated components:

### Types of Prompts:

1. **Zero-shot Prompt**
   - Direct question, no examples.
   - _Example_: “Translate this sentence to French: ‘Hello’”

2. **Few-shot Prompt**
   - Adds examples to improve accuracy.
   - _Example_:
     ```
     English: Hello → French: Bonjour
     English: Good morning → French: Bonjour
     English: Thank you → French: Merci
     ```

3. **Chat Prompt**
   - For chat models like GPT-3.5/GPT-4.
   - Allows messages with roles: system, user, assistant.
   - _Example_:
     - System: "You're a helpful tutor"
     - User: "Explain Quantum Physics in simple terms"

LangChain supports all of these via `PromptTemplate`, `FewShotPromptTemplate`, and `ChatPromptTemplate`.

---

## 🧠 LLMs and Models

LangChain integrates with many LLMs like:
- OpenAI GPT-3.5 / GPT-4
- Anthropic Claude
- Cohere, HuggingFace models

You choose a provider and LangChain wraps it with the ability to plug into prompts, chains, memory, and tools.

---

## 🔗 Chains (LLMChain, SequentialChain)

**Chains** define **how data flows** through your app. Each step is a component like an LLM or a prompt.

- **LLMChain**: A single-step LLM with a prompt → output.
- **SimpleSequentialChain**: Multiple steps one after another.
- **RouterChain**: Routes input to different chains based on conditions.

_Example Flow:_
> User Query → Custom Prompt → LLM → Formatted Output

---

## 🗃️ Embeddings & Vector Indexes

LangChain supports **Retrieval-Augmented Generation (RAG)** using vector databases.

### Concepts:
- **Embeddings**: Convert text to numerical vector form.
- **Vector Store**: Stores embeddings (like Pinecone, FAISS, ChromaDB).
- **Retriever**: Finds relevant documents based on a query.
- **Document Loaders**: Load PDFs, CSVs, Notion, etc.

_Example Use Case_:  
> Store your company documents in FAISS → Ask: “What’s our refund policy?” → Retrieve → Feed to LLM for answer.

---

## 🧠 Memory: Context Awareness

Memory lets LangChain **remember past interactions**, essential for chatbots and assistants.

### Types of Memory:
- `ConversationBufferMemory`: Keeps a chat transcript.
- `ConversationSummaryMemory`: Summarizes past chats.
- `VectorStoreRetrieverMemory`: Stores and retrieves contextually.

_Example_:  
> User: “What’s my order status?”  
> Assistant: “Last time you said your order was #12345. Let me check…”

---

## 🤖 Agents & Tools

**Agents** are LLM-powered decision-makers that can:
- Use tools (e.g., calculators, APIs, search)
- Decide which tool to call based on the query
- Handle complex multi-step logic

### Agent Tools Examples:
- Python REPL for math/code
- Web search
- Custom APIs (e.g., weather, flights)
- Database connectors

_Example_:  
> Question: “What’s the weather in Tokyo, and should I pack a raincoat?”  
> Agent: Calls weather API → Analyzes result → Gives recommendation

---

## 🧩 Putting It All Together

Here’s how a typical LangChain GenAI app is composed:


      [User Input]
           ↓
    [Prompt Template]
           ↓
      [LLMChain]
           ↓
[Memory] ←→ [LLM Output] ←→ [Vector Index/Retriever]
           ↓
        [Agent]
           ↓
      [Final Output]



---

## 📦 Real-World Use Cases

- AI Chatbots with memory + file uploads
- Internal data assistants for analytics
- Code and data documentation bots
- RAG-based Q&A systems
- Agents for workflow automation

---

## ✅ Requirements

- Python 3.8+
- OpenAI Key (or another LLM provider)
- Install LangChain and libraries:
  ```bash
  pip install langchain openai chromadb python-dotenv
