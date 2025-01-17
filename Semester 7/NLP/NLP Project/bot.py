# Updated chatbot implementation following the provided workflow

import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.memory import ConversationBufferMemory
from langchain.llms import FlanT5
import gradio as gr

# Step 1: Load data and preprocess
with open("all_pages_urdu_data first deliverable.json", "r", encoding="utf-8") as file:
    data = json.load(file)

texts = [entry['text'] for entry in data if 'text' in entry]
urls = [entry['url'] for entry in data if 'url' in entry]

# Step 2: Generate embeddings and store in FAISS index
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
embeddings = model.encode(texts, convert_to_tensor=True)
faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
faiss_index.add(np.array(embeddings))

# Metadata for retrieval
metadata = [{"text": texts[i], "url": urls[i]} for i in range(len(texts))]

# Step 3: Query embedding and context retrieval
def query_faiss(query, k=5):
    query_embedding = model.encode([query])
    distances, indices = faiss_index.search(np.array(query_embedding), k)
    results = [metadata[i] for i in indices[0] if i < len(metadata)]
    return results

# Step 4: Generate response with Flan-T5
def generate_response(query, context):
    context_text = "\n".join([doc['text'] for doc in context]) if context else ""
    if context_text:
        prompt = f"Query: {query}\nContext: {context_text}\nResponse in Urdu:"
        llm = FlanT5(model_name="google/flan-t5-large")
        return llm.generate(prompt)
    else:
        return "معذرت، آپ کا سوال ہمارے ڈیٹا کے دائرہ کار میں نہیں ہے۔"

# Step 5: Conversational memory with LangChain
memory = ConversationBufferMemory(return_messages=True)

def chatbot_conversation(user_query):
    if not user_query.strip():
        return "براہ کرم کوئی سوال پوچھیں۔"
    
    # Retrieve context
    retrieved_context = query_faiss(user_query)

    # Generate response
    response = generate_response(user_query, retrieved_context)

    # Add to memory
    memory.add_user_input(user_query)
    memory.add_ai_response(response)

    return response

# Step 6: User interaction and deployment with Gradio
def chatbot_interface():
    def respond(query):
        return chatbot_conversation(query)

    ui = gr.Interface(fn=respond, inputs="text", outputs="text", title="Urdu Chatbot", description="Ask questions about Punjab Police Khidmat Markaz.")
    ui.launch()

if __name__ == "__main__":
    chatbot_interface()
