# https://pypi.org/project/wordcloud/
#!pip install wordcloud
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import os
import random
# from wordcloud import WordCloud, STOPWORDS
from wordcloud import *







class Wordcloud:
    """
    Wordcloud Utilities
    """
    def generate(self, text):
        # Generate a word cloud image
        wordcloud = WordCloud().generate(text)

        # Display the generated image:
        # the matplotlib way:
        import matplotlib.pyplot as plt
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")

        # lower max_font_size
        wordcloud = WordCloud(max_font_size=40).generate(text)
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    def generate01(self, benchmark_name, text, myStopwords = None, file_name = "wordcloud"):

        def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
            return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
        
        stopwords = set(STOPWORDS)
        """
        # Add some default stopwords specific to the text
        stopwords.add("one")
        stopwords.add("said")
        stopwords.add("will")
        stopwords.add("little")
        stopwords.add("now")
        stopwords.add("well")
        stopwords.add("see")
        stopwords.add("must")
        stopwords.add("time")
        #print(stopwords)
        """
        if myStopwords != None:
            for word in myStopwords:
                stopwords.add(word)
                
        wc = WordCloud(width=1600, height=800, random_state=42, colormap="viridis").generate(text)
        
        #wc = WordCloud(max_words=10, stopwords=stopwords, margin=10, random_state=1).generate(text)
        # store default colored image
        default_colors = wc.to_array()
        #plt.title("Word Cloud")
        #plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
        #plt.imshow(wc.recolor(random_state=3), interpolation="bilinear")
        plt.axis("off")
        plt.figure(figsize=(15, 10))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        # wc.to_file(".\\" + benchmark_name + "\\results\\" + file_name + ".png")
        wc.to_file("wordcloud.png")
        #plt.show()