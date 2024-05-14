import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split  
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import ast as ast
# Abstract Syntax Tree 
import nltk as nltk
from nltk.stem.porter import PorterStemmer
#Natural Language Toolkit
from tkinter import *
import tkinter

#Append only the genre_names from the genre object in the dataFrame
def convert(obj):
    li=[]
    for i in ast.literal_eval(obj):
        li.append(i['name'])
    return li

#Append only the actor_names from the cast object in the dataFrame
def convert_cast(obj):
    lis=[]
    number=0
    for j in ast.literal_eval(obj):
        if number !=4:
            lis.append(j['name'])
            number=number+1
        else:
            break
    return lis

def find_director(obj):
    director=[]
    for i in ast.literal_eval(obj):
        if i['job']=="Director":
            director.append(i['name'])
    return director

def join_b(x):
    return ' '.join(x)


def stem(input):
    input_list=[]
    for i in input.split():
        input_list.append(ps.stem(i))
    return " ".join(input_list)


