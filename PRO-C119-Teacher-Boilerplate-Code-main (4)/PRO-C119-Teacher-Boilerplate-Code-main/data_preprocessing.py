#Text Data Preprocessing Lib
import nltk

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle
import numpy as np

# function for appending stem words
words =[]
classes =[]
word_tags_list=[]
ignore_words =["?","!","@","&",",",".","'s","'m"]

train_data_file = open("intents.json").read()
intents = json.loads(train_data_file)

def get_stem_words(words,ignore_words):
       stem_words =[]
       for word in words:
                if word not in ignore_words:
                        w = stemmer.stem(word.lower())
                        stem_words.append(w)
        return stem_words

        

    
        # Add all words of patterns to list
        
        # Add all tags to the classes list
         

#Create word corpus for chatbot

