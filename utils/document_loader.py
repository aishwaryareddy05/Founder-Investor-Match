import pandas as pd
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
import os

# Set your API key
os.environ["GOOGLE_API_KEY"] = "api_key"

# Load the CSV files
investors_df = pd.read_csv('investors.csv')
founders_df = pd.read_csv('founders.csv')

# Define relevant fields
investor_fields = ['investor_name', 'min_investment_usd','max_investment_usd', 'preferred_industries','preferred_stages', 'investment_thesis']
founder_fields = ['startup_name','product_description', 'industry', 'startup_stage', 'funding_required_usd','traction_summary','business_model']

# Combine fields into text chunks
def df_to_documents(df, fields):
    docs = []
    for _, row in df.iterrows():
        content = " | ".join(str(row[field]) for field in fields if pd.notna(row[field]))
        metadata = {"name": row[fields[0]]}
        docs.append(Document(page_content=content, metadata=metadata))
    return docs

# Convert each profile to a LangChain Document
investor_docs = df_to_documents(investors_df, investor_fields)
founder_docs = df_to_documents(founders_df, founder_fields)

# Use GoogleGenerativeAIEmbeddings
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Create vector database using Chroma
investor_vectorstore = Chroma.from_documents(investor_docs, embedding, persist_directory="investor_chroma_db")
founder_vectorstore = Chroma.from_documents(founder_docs, embedding, persist_directory="founder_chroma_db")

# Save to disk
investor_vectorstore.persist()
founder_vectorstore.persist()

print("✅ Vector databases created and saved!")