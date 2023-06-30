import sys

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

import config


def run_query(query: str):
    db = Chroma(
        persist_directory=config.DOCDB,
        embedding_function=OpenAIEmbeddings(),
    )

    llm = OpenAI(
        openai_api_key=config.OPENAI_API_KEY,
        temperature=0.0,
        # model='gpt-3.5-turbo',
        # model='text-davinci-003',
        # model='text-davinci-002',
    )

    print(f"Running query: '{query}'")
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(),
    )

    prompt = f"""
    You are a digital assistant assisting users in finding information in a collection of documents.
    You are being asked by a user to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Always include the name of the source documents from which you found the answer as references.
    Answer the following question: {query}
    """

    res = chain.run(prompt)
    print(f"Response: '{res}'")


if __name__ == "__main__":
    # Use command line args if provided
    query = None
    args = sys.argv
    args.pop(0)
    if len(args) > 0:
        query = ' '.join(args)

    # Override query here
    if query is None:
        query = 'When was the Cologne Cathedral built and how tall is it?'

    run_query(query)
