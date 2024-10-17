# SDS Chatbot with RAG Pipeline

This repository contains a chatbot that can be used with or without a Retrieval-Augmented Generation (RAG) pipeline. The chatbot interacts with users and responds based on context provided. It can either fetch responses directly from a language model (without RAG) or leverage a vector store to retrieve relevant context from predefined knowledge (with RAG).

## Features
- **Chat Mode**: A simple chatbot that responds to questions based on predefined prompts.
- **RAG Mode**: Combines a sentence embedding model and vector store to provide context-based responses by retrieving the most relevant information from the knowledge base.

---

## Setup Guide

### Prerequisites
- Google Collab account
- A valid API key for Groq's GPT model

### Configuration

Replace the following placeholder with your Groq API key in the code:
```python
GROQ_API_KEY = "your-api-key"
```

Update the model names as necessary:
```python
CHAT_MODEL         = "llama3-70b-8192"
EMBEDDING_MODEL    = "sentence-transformers/all-MiniLM-L6-v2"
```

### Usage

#### Running the Chatbot in Standard Mode

This mode allows users to ask questions, and the chatbot responds factually based on the predefined prompt.

1. Run the chatbot in standard mode (without RAG):
    ```bash
    chat()
    ```

2. The chatbot will greet you and allow you to ask questions:
    ```plaintext
    Welcome to ChatGPT! Feel free to ask me anything!
    ```

3. Type `exit` or `quit` to stop the chatbot.

#### Running the Chatbot with RAG Pipeline

The RAG pipeline allows the chatbot to answer questions based on retrieved-context from the knowledge base.

1. Place your knowledge file (`story.txt`) in the same directory as the chatbot script.
2. Run the chatbot in RAG mode:
    ```bash
    rag_pipeline()
    ```

3. The chatbot will retrieve the most relevant context from the `story.txt` file to answer user queries:
    ```plaintext
    Welcome to the SDS Story chatbot! Feel free to ask me anything about the SDS workshop members!
    ```

4. Type `exit` or `quit` to stop the chatbot.

---

## Project Structure

- **`retrieval-augemnted-generation-example.ipynb`**: Main script containing the chatbot and RAG pipeline.
- **`story.txt`**: Knowledge base containing contextual information for RAG.

---

## How It Works

### Vector Store
The vector store stores embeddings of chunks of text from the knowledge base and allows similarity-based retrieval of the most relevant text for the given query.

### Text Splitter
The `TextSplitter` class helps break down large blocks of text into smaller chunks for better processing and embedding generation.

### Embedding Model
This model is responsible for generating vector embeddings using the `sentence-transformers` library. These embeddings are used for similarity search during RAG.

### RAG Pipeline
1. **Contextual Knowledge**: The chatbot uses predefined contextual knowledge stored in `story.txt`.
2. **Embeddings**: Text chunks from the knowledge base are embedded using a sentence transformer model.
3. **Retrieval**: The chatbot retrieves relevant text based on query embeddings.
4. **Response Generation**: The chatbot builds a prompt combining the retrieved context and user query to fetch a response.

---

### Step-by-Step Guide: How to Create a Groq API Key

To use Groq's API, you’ll first need to generate an API key, which allows your application to authenticate and make requests to Groq's services. Follow the steps below to create your API key.

---

### Step 1: Sign Up or Log In to Groq

1. **Visit Groq's official website**:  
   Navigate to [https://www.groq.com](https://www.groq.com).
   
2. **Sign Up** (if you don’t have an account):  
   - Click on the **Sign Up** button at the top right corner of the homepage.
   - Fill in your details (email, password, etc.) to create an account.
   - Verify your email address, if required, by following the instructions sent to your email.
   
   **Log In** (if you already have an account):  
   - Click on the **Log In** button and enter your credentials.

---

### Step 2: Access the API Management Dashboard

1. After logging in, navigate to the **API Management** section.
   - This can usually be found under the **Developer** or **Account Settings** menu, depending on the platform layout.

2. Once there, locate the **API Keys** section, which allows you to manage and generate keys for accessing Groq's APIs.

---

### Step 3: Generate a New API Key

1. Click on the **Create New API Key** button.

2. Provide a **name** for your API key (this could be something like `MyProject-APIKey` to easily identify its use).

3. Select the **permissions** for the API key (if applicable).  
   - For most cases, you can leave it as default or select the appropriate permissions your project requires.

4. Click **Generate** or **Create**.

---

### Step 4: Copy and Store Your API Key

1. Once the API key is generated, **copy** the API key immediately.
   
   **Note**: For security reasons, most platforms will only show the key once. Be sure to store it in a safe place like a password manager or a secure configuration file.

2. **Store it safely**: Ensure that the API key is not hard-coded directly into public repositories. Use environment variables or secure storage methods (e.g., `.env` files).

---

### Step 5: Set Up API Key in Your Project

To use the API key in your project, follow these steps:

**In Your Code**:  
   Use the API key in your code when initializing the client:
   ```python
   GROQ_API_KEY = "your-api-key"
   ```







---
