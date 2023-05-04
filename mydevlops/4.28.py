import os
from api import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import SimpleSequentialChain

#loader = UnstructuredHTMLLoader("oprator's manual.html")
#documents = loader.load()
#text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=100)
st.title('You can optimize your content and convert to qualified DITA XML here, just input your content below')
prompt_documents = st.text_area ( 'Input a piece of text, I can help you optimize it and convert to dita xml format' )
prompt_documents1 = st.text_area ( 'Input a piece of dita xml text, I can help you optimize it\'s content' )

os.environ["OPENAI_API_KEY"]=apikey
llm = OpenAI(temperature=0.7,max_tokens=2500)

template1 = """
You are a professional technical writer, now I want you to optimize the dita xml con which means to check and correct the content to make sure that:

 Grammar is correct.
 Spelling is correct and consistent.
 word is rightly used.
 
and just output the optimized content with a proper title.

please do the task based on text:{text1}.
"""
prompt1=PromptTemplate(
    template=template1,
    input_variables=["text1"])

template2 = """
You are a professional technical writer, now I want you to recognize the DITA type first and then convert the text into a qualified DITA XML document with a DITA topic to be organized and structured.

please do the task based on text:{text2}.
"""
prompt2=PromptTemplate(
    template=template2,
    input_variables=["text2"])

template3 = """
You are a professional technical writer, now I want you to output a corresponding formalized markdown style text, the output should be structured and easy to understand.

please do the task based on text:{text3}.
"""
prompt3=PromptTemplate(
    template=template3,
    input_variables=["text3"])

template4 = """
You are a professional technical writer, now I want you to make the text more structured and easy to understand.

please do the task based on text:{text4}.
"""
prompt4=PromptTemplate(
    template=template4,
    input_variables=["text4"])

template5 = """
You are a professional technical writer, now I want you to recognize the DITA type first and then convert the text into a qualified DITA XML document with a DITA topic to be organized and structured.

please do the task based on text:{text5}.
"""
prompt5=PromptTemplate(
    template=template5,
    input_variables=["text5"])

chain1 = LLMChain(llm=llm, prompt=prompt1)
chain2 = LLMChain(llm=llm, prompt=prompt2)
chain3 = LLMChain(llm=llm, prompt=prompt3)
chain4 = LLMChain(llm=llm, prompt=prompt4)
chain5 = LLMChain(llm=llm, prompt=prompt5)
sequential_chain=SimpleSequentialChain(chains=[chain1,chain2])
sequential_chain2=SimpleSequentialChain(chains=[chain1,chain5])
if prompt_documents:
    #for i in range(len(documents)):
    response1=sequential_chain.run(prompt_documents)
    #response2=chain4.run(response1)
 
    
    # Display the results
    st.write(response1)
   # st.text_area("Input from last cycle", value=response1)
    #st.write(response2)
if prompt_documents1:
    response2=chain5.run(prompt_documents1)
    st.write(response2)