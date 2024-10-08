import re
from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from pydantic import BaseModel
from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core.query_pipeline import QueryPipeline
from dotenv import load_dotenv
import os
import ast

load_dotenv()

llm = Ollama(model="mistral", request_timeout=30.0)

parser = LlamaParse(result_type="markdown")

prompt = input("Enter a file type to look at in /data or a url to scrape: ")

if re.search(r"https?://", prompt):
    print("Scraping URL",prompt)
    documents = SimpleWebPageReader(html_to_text=True).load_data([prompt])
else:
    print("Looking at file type", prompt)
    file_extractor = {prompt: parser}
    documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

#file_extractor = {".pdf": parser}
#file_extractor = {".docx": parser}
#documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

##documents = SimpleWebPageReader(html_to_text=True).load_data(["https://www.bbc.com/news"])

embed_model = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = vector_index.as_query_engine(llm=llm)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = query_engine.query(prompt)
    print(result)
