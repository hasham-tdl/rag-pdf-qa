from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

INDEX_PATH = "index/book_faiss"

def load_retriever():
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vectorstore = FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore.as_retriever(search_kwargs={"k": 3})


def create_rag_chain(retriever):
    prompt = ChatPromptTemplate.from_template(
        """
You are an assistant that answers questions strictly using the provided source context.
Use the same context or answer for question that can be implicitely catergorized together.
If the answer is not present in the context, say:
"I cannot find this information in the source."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    llm = OllamaLLM(
        model="llama3.1",
        temperature=0
    )

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return rag_chain


if __name__ == "__main__":
    retriever = load_retriever()
    rag_chain = create_rag_chain(retriever)

    while True:
        query = input("\nAsk a question (or 'exit'): ")
        if query.lower() == "exit":
            break

        answer = rag_chain.invoke(query)
        print("\nAnswer:\n", answer)
