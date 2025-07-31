from fastapi import FastAPI, Query
from rag_chain import create_chain
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
chain = create_chain()


@app.get("/ask")
def ask(query: str = Query(...)):
    """
    Endpoint to ask a question to the RAG system.
    """
    result = chain.invoke(query)
    return {"response": result}
