from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores.redis import Redis
from langchain_community.embeddings import OpenAIEmbeddings


def create_chain():
    prompt = PromptTemplate(
        input_variables=["query"],
        template="Answer the following query: {query}"
    )

    llm = OpenAI(temperature=0.7)

    chain = prompt | llm

    return chain


def get_vector_store():
    return Redis.from_texts(
        texts=["Some doc about your domain..."],
        embedding=OpenAIEmbeddings(),
        redis_url="redis://localhost:6379"
    )
