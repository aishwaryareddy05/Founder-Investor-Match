from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def embed_query(state):
    embedded = embedding.embed_query(state["query"])
    return {"query": state["query"], "embedding": embedded}
