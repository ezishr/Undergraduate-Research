import json
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import textstat
import textblob
import os
import ipynb
import import_ipynb
import contextlib
import random
import re
import gensim.parsing.preprocessing as preprocessing

# AI
import google.generativeai as genai
os.environ["GEMINI_API_KEY"] = "AIzaSyCM-GWMhMPoBZpvlXWqKr5nKnY02OIVdf4"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

from groq import Groq
os.environ["GROQ_API_KEY"] = "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"
client = Groq(
    api_key=os.environ['GROQ_API_KEY'],
)


import time


# Packages to deal with NLP
import spacy
nlp = spacy.load('en_core_web_sm')
import nltk
from nltk.corpus import words, brown
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk
from nltk.stem import WordNetLemmatizer

# Comment out the two below if you haven't downloaded words and brown
# nltk.download('words')
# nltk.download('brown')

english_words = set(words.words())
from textblob import TextBlob


import matplotlib as plt
from pathlib import Path

pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', 20)