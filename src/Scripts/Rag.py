import os                               # a way to interact with the operating system
import pandas as pd                     # allows us to manipulate data
import numpy as np                      # used to preform mathematical operations
import matplotlib as mlt                # helps create graphs
from matplotlib import pyplot as plt    # used to help with visualizations
import csv                              # helps to read csv files
from collections import Counter         # counts and stores elements in a dictionary
import requests                         # allows to work with websites
import re                               # allows to use regular expressions
from statistics import mean
from math import sqrt
import sys
import json
import ast
import llama_index
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from llama_index.llms import openai
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import sys
print("dog")
print(sys.executable)


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables
load_dotenv()  # Add this to load OpenAI API key from .env file


documents = SimpleDirectoryReader("./data").load_data()


vectorstore = VectorStoreIndex.from_documents(documents)

query_engine = vectorstore.as_query_engine()

def use_rag(query):
    try:
        query_answer = query_engine.query(query)
        print(query)
        print(query_answer)
        # Ensure proper JSON formatting
        print(json.dumps(query_answer))  # This is the only print statement that should output results
        sys.stdout.flush()

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        use_rag(sys.argv[1])
