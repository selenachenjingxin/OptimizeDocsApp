import os
from api import apikey
from langchain.document_loaders import UnstructuredWordDocumentLoader
loader = UnstructuredWordDocumentLoader("oprator's manual.docx")
pages = loader.load_and_split()