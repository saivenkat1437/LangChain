# 🤖 LangChain Prompts & Chatbots

This repository provides a clear and beginner-friendly understanding of how **LangChain** can be used to build intelligent systems with **prompts**, **chains**, and **chatbot applications**.

---

## 📚 Table of Contents

- [📖 Introduction](#-introduction)
- [🧠 What Are Prompts?](#-what-are-prompts)
- [🧩 Types of Prompt Templates in LangChain](#-types-of-prompt-templates-in-langchain)
  - [1. Basic Prompt Template](#1-basic-prompt-template)
  - [2. Chat-Based Prompt Template](#2-chat-based-prompt-template)
  - [3. Few-Shot Prompt Template](#3-few-shot-prompt-template)
- [🔗 LLM Chains (Connecting Prompt + LLM)](#-llm-chains-connecting-prompt--llm)
- [💬 Chatbot Example](#-chatbot-example)
---

## 📖 Introduction

LangChain is a powerful Python framework for building applications powered by **Large Language Models (LLMs)** like GPT-4. It simplifies tasks like prompt engineering, document search, memory handling, and multi-step reasoning.

---

## 🧠 What Are Prompts?

Prompts are instructions or examples that tell an LLM what kind of output is expected. They are like **questions** or **command templates** you give to the model.

For example, a prompt could be:

> “Translate the following English text to French: ‘Good morning.’”

LangChain lets you structure such prompts in reusable, scalable, and dynamic ways.

---

## 🧩 Types of Prompt Templates in LangChain

LangChain supports different types of prompts depending on the use case:

---

### 1. **Basic Prompt Template**

Used when you want to dynamically insert variables into a fixed sentence structure.

**Example:**  
You want to ask: “What is the capital of India?”  
But for multiple countries — so you create a template like:  
“**What is the capital of {country}?**”  
LangChain fills in `{country}` based on input.

---

### 2. **Chat-Based Prompt Template**

Useful when working with **chat models** like GPT-4 or GPT-3.5-turbo.

These prompts are structured into different roles:
- **System:** Describes the assistant’s behavior (e.g., “You are a helpful assistant.”)
- **User:** Actual input from the user.
- **Assistant:** Previous model responses (if any).

**Example Conversation Structure:**

- **System:** You are a grammar expert.
- **User:** Fix this sentence: “he go to market yesterday”

This structure improves output quality for chat models.

---

### 3. **Few-Shot Prompt Template**

When you want the LLM to learn from **examples** before it answers.

**Example:**

Provide examples like:
- “2 + 2 = 4”
- “3 + 5 = 8”

Then ask:  
> “What is 7 + 6?”

This approach is powerful for classification, Q&A, and logic tasks.

---

## 🔗 LLM Chains (Connecting Prompt + LLM)

A **chain** in LangChain is a combination of:
1. A prompt (what to say)
2. A model (who to say it to)
3. Logic (what to do with the answer)

Think of it as a **pipeline** where input goes in, the model processes it based on the prompt, and the output is returned.

**Example Use Case:**  
Ask “What’s the weather in New York today?” and send that to the model through a chain. The model replies, and you display the answer.

---

## 💬 Chatbot Example

LangChain allows building memory-based chatbots.

These bots can:
- Remember past conversations
- Respond in context
- Generate Python code
- Answer business-specific questions (if connected to your data)

**Example Use Case:**  
Build a virtual assistant that:
- Greets the user
- Answers FAQs about your company
- Summarizes documents
- Books meetings (with integrations)

---

## 🧱 Requirements

To use LangChain, you typically need:
- Python 3.8 or newer
- An OpenAI API key (or another LLM provider)
- LangChain and supporting packages

---

## ⚙️ Setup Instructions

1. Clone this repo.
2. Create a Python virtual environment.
3. Install dependencies from `requirements.txt`.
4. Add your API key in a `.env` file:
   ```env
   OPENAI_API_KEY=your_key_here
