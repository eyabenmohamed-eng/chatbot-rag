                              Chatbot PDF intelligent (Système RAG)

Projet d'Intelligence Artificielle consistant à créer une interface web interactive capable de répondre à des questions complexes sur n'importe quel document PDF en utilisant la méthode **RAG (Retrieval-Augmented Generation)**.

                      Membres de l'équipe:
               BENMOHAMED EYA & HAFYEN NOURELHOUDA
 Fonctionnalités du Projet
Interface Web : Développée avec Streamlit pour une utilisation simple et intuitive.
Extraction de texte : Découpage du PDF en segments pertinents (Chunks) pour optimiser la recherche sémantique.
Modèle Génératif (LLM) : Utilisation de l'API OpenAI / LangChain pour générer des réponses précises et contextualisées basées uniquement sur le document.
 Comment lancer le projet en local
Suivez ces étapes pour exécuter la démo sur votre machine :
 1. Cloner le projet
  git clone [https://github.com/eyabenmohamed-eng/chatbot-rag.git](https://github.com/eyabenmohamed-eng/chatbot-rag.git)
  cd chatbot-rag

2 — Créer une clé API :
  
   Cliquez sur API Keys dans le menu gauche
  
   Cliquez Create API Key
  
   Copiez la clé qui commence par gsk_...
  
   notepad .env    (powershell)
  
   GROQ_API_KEY=gsk_sa_cle_a_elle   (block_notes)

3.pip install -r requirements.txt   (powershell)


4.streamlit run app.py    (powershell)
L'application s'ouvrira automatiquement dans votre navigateur à l'adresse http://localhost:8501.

