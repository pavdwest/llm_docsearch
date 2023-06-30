import os
import glob
from pathlib import Path
from typing import List, Type
import shutil

from langchain.schema import Document
from langchain.document_loaders.base import BaseLoader
from langchain.document_loaders import (
    PyPDFium2Loader,
    UnstructuredHTMLLoader,
    TextLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import config


def load_document(path: str) -> List[Document]:
    """Loads and splits a file using an appropriate Document Loader.

    Args:
        path (str): Relative path to file.

    Returns:
        List[Document]: List of documents that can be consumed by a VectorStore
    """
    match Path(path).suffix:
        case '.pdf':
            return PyPDFium2Loader(path).load_and_split()
        case '.html':
            return UnstructuredHTMLLoader(path).load_and_split()
        case _:
            return TextLoader(path).load_and_split(
                text_splitter=RecursiveCharacterTextSplitter(
                    chunk_size=1024,
                    chunk_overlap=64,
                )
            )


def create_documents(root_path: str) -> List[List[Document]]:
    """Utility function that finds all files in a root folder recursively and loads them up as documents.
    Makes async implementation simpler in the future.

    Args:
        root_path (str): Relative path to the root

    Returns:
        List[Document]: _description_
    """
    return [load_document(path) for path in glob.glob(f"{root_path}/**/*.*", recursive=True)]


def train():
    # Check if there are documents to train on
    source_documents = [path for path in glob.glob(f"{config.DOCPATH}/**/*.*", recursive=True)]

    if not source_documents:
        print(f"No training docs found in '{config.DOCPATH}'. Exiting.")
    else:
        print('Delete existing db...')
        if Path(config.DOCDB).exists():
            shutil.rmtree(config.DOCDB)

        # Encode docs
        print(f"Loading {len(source_documents)} documents...")
        documents = [load_document(path) for path in source_documents]

        # Create db
        print('Creating vector db...')
        db = Chroma().from_documents(
            [doc for doclist in documents for doc in doclist],
            embedding=OpenAIEmbeddings(),
            persist_directory=config.DOCDB
        )
        db.persist()
        print('Done!')


if __name__ == "__main__":
    train()
