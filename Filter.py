# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:05:13 2019

@author: kcgov
"""

import pandas as pd 
import numpy as np
import json
import nltk

Food_Composition=pd.read_csv("Food Composition.csv")

Food_Words = Food_Composition.iloc[3:,0:2]

Rows=Food_Words.shape[0]
j=0
p=0

is_noun = lambda pos: pos[:2] == 'NN'

Food_Dict={}
Food_List = []
for i in range(Rows-1):
    Department = Food_Words.iloc[i,0]
    Word= Food_Words.iloc[i,1]
    Word = Word.split(',')[0]
    Word = Word.split('(')[0]
    tokenized = nltk.word_tokenize(Word)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    
    if not (pd.isnull(Department)):
        
        key = Department
        Food_Dict[key]=Food_List
        for word in nouns:
            Food_List.append(word)

    else:
        for word in nouns:
            Food_List.append(word)



for i,lists in Food_Dict.items():
    list_set = set(lists)
    temp_list = list(list_set)
    Food_Dict[i] = temp_list
        
with open('Word_Dict.txt', 'w') as file:
     file.write(json.dumps(Food_Dict))


    