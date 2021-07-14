# -*- coding: utf-8 -*-
"""ComicBookRemendator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MMFk2NjQF0EaCMpAbsQIf-4N2YSZ_WnU
"""

#Importing All Required Libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#Uploading The File .csv aka Dataset
from google.colab import files
files.upload()

#Displaying all data inside dataset
df = pd.read_csv('Manga_Data.csv')
df

#creating new column for Comics ID ps:You need this!
df['Manga_id'] = range(0,51)

#checking if the column has been created
df

#Collecting all Colmns that you want to use in cosine similarity
Columns = ['Title', 'Genre', 'Synopsis']

#Create Function to combine all of that(Previous Code) in singgle string
def get_important_feature(data):
  important_features = []
  for i in range(0, data.shape[0]):
    important_features.append(data['Title'][i]+' '+data['Genre'][i]+' '+data['Synopsis'][i])

  return important_features

#Create Column 'important_features' to hold 'def' function
df['important_features'] = get_important_feature(df)

df.head(3)

#Conver Text the text to a matrix token
cm = CountVectorizer().fit_transform(df['important_features'])

cm.shape

#Get cosine similarity matrix from the matrix token
cs = cosine_similarity(cm)

#print cosine similarity matrix ps: 1 indicates 100% similarity on that index and row
print(cs)

cs.shape

#Getting the comic title
title = 'Grand Blue'

#finding the comic id
manga_id = df[df.Title == title]['Manga_id'].values[0]

#Create List Of Enumeration for similarity score like this [ (movie_id, similarity scores), (...) ]
scores = list(enumerate(cs[manga_id]))

#Sort the score
sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
sorted_scores = sorted_scores[1:]

#print the sorted scores
print(sorted_scores)

#Create Loop to print recomended movies
j=0
print('7 Most Recomended Manga After Reading', title, 'are:\n')
for item in sorted_scores:
  manga_title = df[df.Manga_id == item[0]]['Title'].values[0]
  print(j+1, manga_title)
  j=j+1
  if j>6:
    break