# 🧩 LangChain Framework — Notes

## 🔹 What is LangChain?

LangChain is a framework for building applications powered by Large Language Models (LLMs).

It provides abstractions and utilities to:

- **Prompting** → create reusable, structured prompts
- **LLM Wrappers** → connect to models (OpenAI, Groq, HuggingFace, etc.)
- **Chains** → connect multiple steps (e.g., retrieval → summarization → answer)
- **Memory** → make LLMs stateful (conversation history)
- **Retrievers / Vector Stores** → fetch relevant context (RAG)
- **Agents + Tools** → let LLMs decide which actions/tools to use
- **Graph + Knowledge Integration** → enhance reasoning via knowledge graphs

## 🔹 Basic Implementation

- Set up FastAPI backend
- Integrated LangChain components:

  ```python
  from langchain_groq import ChatGroq
  from langchain.prompts import PromptTemplate
  ```

  - ChatGroq → LLM wrapper for Groq's Llama model
  - PromptTemplate → structured prompts for summarization + Q&A

- Created simple endpoints:
  ```python
  @app.post("/summarize/")       # naive character-based summarizer
  @app.post("/summarize_llm/")   # LLM summarizer with word constraints
  @app.post("/ask/")             # LLM answers based on text + question
  ```

👉 This is basic LangChain usage — using LLM wrappers + prompt templates.

## 🔹 What LangChain Can Do (Beyond This)

- **Chains**: Combine multiple steps (retrieval → LLM → post-processing)
- **Memory**: Maintain conversation across multiple requests
- **RAG (Retrieval Augmented Generation)**: Use vector DB (like Chroma) to provide context
- **GraphRAG**: Use a graph DB (like Neo4j) for reasoning over entities + relationships
- **Agents**: Give LLMs access to tools (DB queries, web search, APIs)
- **Workflows**: Orchestrate hybrid pipelines (structured data + unstructured docs + LLM reasoning)

## 🔹 Roadmap / Next Steps (Gist)

### 1. Retrieval Chains (RAG)

```python
# Example RAG pipeline
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

# Ingest → chunk → embed → store
documents = load_and_split_files()
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=OpenAIEmbeddings()
)

# Retrieve → generate
retriever = vectorstore.as_retriever()
docs = retriever.get_relevant_documents(query)
prompt = f"Context: {docs}\n\nQuestion: {query}"
result = llm(prompt)
```

### 2. Graph RAG

```python
# Example GraphRAG setup
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph()
graph.add_entities_and_relations(documents)
cypher_query = "MATCH path=shortestPath(...)"
graph_context = graph.query(cypher_query)
```

### 3. Agents (Tool-Using LLMs)

```python
from langchain.agents import Tool, AgentExecutor

tools = [
    Tool(
        name="Search",
        func=search_api,
        description="Useful for current events"
    ),
    Tool(
        name="Calculator",
        func=calculator,
        description="For math calculations"
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
agent.run("What's the weather in Tokyo today?")
```

### 4. GenAI Patterns

- Summarization → (already done)
- Q&A over text → (already done)
- Conversational memory → (chatbots)
- Multi-modal pipelines → text + images
- Workflow orchestration → RAG + Agents + external APIs
