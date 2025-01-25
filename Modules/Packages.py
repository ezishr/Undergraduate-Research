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
# import gensim.parsing.preprocessing as preprocessing


import time


# Packages to deal with NLP
# import spacy
import nltk
from nltk.corpus import words, brown

# Comment out the two below if you haven't downloaded words and brown
# nltk.download('words')
# nltk.download('brown')

english_words = set(words.words())
from textblob import TextBlob


import matplotlib as plt
from pathlib import Path

pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', 20)