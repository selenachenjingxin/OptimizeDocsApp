import os

import streamlit as st
import openai
import oai
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

openai.api_key= os.getenv("OPENAI_API_KEY") 

#loader = UnstructuredHTMLLoader("oprator's manual.html")
#documents = loader.load()

#text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=100)
st.title('You can optimize your content or convert to qualified DITA XML here, just input your content below')

prompt_documents = st.text_area ( 'Input a piece of text, I can help you optimize it\'s structure and content' )
prompt_documents1 = st.text_area ( 'Input a piece of text, I can help you convert it to dita xml format' )

llm = OpenAI(temperature=0.7,max_tokens=2500)

## 优化内容
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

# 易懂+结构化
template4 = """
You are a professional technical writer, now I want you to make the text more structured and easy to understand.

please do the task based on text:{text4}.
"""
prompt4=PromptTemplate(
    template=template4,
    input_variables=["text4"])

## 转化为markdown
template3 = """
You are a professional technical writer, now I want you to convert the text to a corresponding formalized markdown style text.

please do the task based on text:{text3}.
"""
prompt3=PromptTemplate(
    template=template3,
    input_variables=["text3"])

#转化为dita
template2 = """
You are a professional technical writer, now I want you to recognize the DITA type first and then convert the text into a qualified DITA XML document.
please do the task based on text:{text2}.
"""
prompt2=PromptTemplate(
    template=template2,
    input_variables=["text2"])

# 转化为dita
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


sequential_chain=SimpleSequentialChain(chains=[chain1,chain4])
sequential_chain2=SimpleSequentialChain(chains=[chain1,chain4,chain3])

if prompt_documents:
    response2=sequential_chain2.run(prompt_documents)
    with st.container():
        st.write(response2)

if prompt_documents1:
    #for i in range(len(documents)):
    response1=chain2.run(prompt_documents1)
    #response2=chain4.run(response1)
    
    # Display the results
    with st.container():
        st.write(response1)

