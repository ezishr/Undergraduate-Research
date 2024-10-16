import json
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import textstat
import textblob
import os
<<<<<<< HEAD
import contextlib
import ipynb

# Packages to deal with NLP
import spacy
import nltk
from nltk.corpus import words, brown

# Comment out the two below if you haven't downloaded words and brown
# nltk.download('words')
# nltk.download('brown')

english_words = set(words.words())
from textblob import TextBlob
=======

>>>>>>> fd3f0875f31ff093c131198d4aab9f530cf5ca5d

import matplotlib as plt
from pathlib import Path

pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', 10)