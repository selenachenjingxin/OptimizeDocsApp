import os
import oai
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from langchain.memory import ConversationBufferMemory



os.environ["OPENAI_API_KEY"]=openai.api.key

st.title('My own Website')
prompt_input=st.text_input('write a piece of text，I can help you optimize it')


## prompt templates
template1 = """
You are a professional technical writer, now I want you to optimize which means to check and correct the content to make sure that:

 Grammar is correct.
 Spelling is correct and consistent.
 word is rightly used.
 
and just output the optimized content with a proper title.

please do the task based on text:{text1}.
"""
prompt1=PromptTemplate(
    template=template1,
    input_variables=["text1"],)

#template2_script=PromptTemplate(
   # input_variables=['title'],
   # template="write me a youtube script whose title is {title}")

'''## memory
memory1=ConversationBufferMemory(input_key="topic",memory_key='chat_history')
memory2=ConversationBufferMemory(input_key="title",memory_key='chat_history',)

llm=OpenAI(temperature=0.9)
chain1=LLMChain(llm=llm,prompt=template1_title,output_key='title',memory=memory1,verbose=True)
chain2=LLMChain(llm=llm,prompt=template2_script,output_key='script',memory=memory2,verbose=True)
sequential_chain=SequentialChain(chains=[chain1,chain2],input_variables=['topic'],output_variables=['title','script'],verbose=True)
if prompt_input:
    response=sequential_chain({"topic":prompt_input})
    st.write(response['title'])
    st.write(response['script'])

    with st.expander('message history'):
        st.info(memory1.buffer)
        st.info(memory2.buffer)'''

llm=OpenAI(temperature=0.9)
chain1=LLMChain(llm=llm,prompt=template1,output_key='title',verbose=True)

p=chain1.run