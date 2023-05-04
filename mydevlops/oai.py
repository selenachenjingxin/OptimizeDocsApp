# Import from standard library
import os
import logging

# Import from 3rd party libraries
import openai
import streamlit as st

# Assign credentials from environment variable or streamlit secrets dict
openai.api_key = os.getenv("OPENAI_API_KEY") 