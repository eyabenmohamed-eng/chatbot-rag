import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain.embeddings.base import Embeddings
import tempfile
import os

class SimpleEmbeddings(Embeddings):
    def embed_documents(self, texts):
        import hashlib
        result = []
        for text in texts:
            vec = [float(int(hashlib.md5((text+str(i)).encode()).hexdigest(),16) % 1000) / 1000 for i in range(384)]
            result.append(vec)
        return result
    def embed_query(self, text):
        return self.embed_documents([text])[0]

st.title("Chatbot PDF - Systeme RAG")
st.write("Uploadez un PDF et posez vos questions !")
uploaded_file = st.file_uploader("Choisir un fichier PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(uploaded_file.read())
        tmp_path = f.name
    with st.spinner("Chargement et indexation du PDF..."):
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)
        vectorstore = SKLearnVectorStore.from_documents(chunks, SimpleEmbeddings())
        retriever = vectorstore.as_retriever()
        llm = ChatGroq(model="llama-3.1-8b-instant")
    st.success(f"PDF indexe avec succes ! ({len(chunks)} chunks)")
    question = st.text_input("Votre question :")
    if question:
        with st.spinner("Recherche en cours..."):
            docs_result = retriever.invoke(question)
            context = "\n".join([d.page_content for d in docs_result])
            messages = [
                SystemMessage(content="Reponds en francais en te basant uniquement sur ce contexte:\n" + context),
                HumanMessage(content=question)
            ]
            answer = llm.invoke(messages)
            st.success(answer.content)
    os.unlink(tmp_path)
