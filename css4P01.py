#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:15:18 2024

@author: adila
"""
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
df = pd.read_csv("movie_dataset.csv")
print(df.info())
print(df.describe()) 
#column names spaces change
df.rename(columns={"Runtime (Minutes)": "Runtime(Minutes)",
                   "Revenue (Millions)": "Revenue(Millions)"}, inplace=True)
#print(df.info())

#print(df.isnull().sum())
#print(len(df))

# filling the NaN values with the average of resepective columns
re_m = df["Revenue(Millions)"].mean() # mean of the revenue
df["Revenue(Millions)"].fillna(re_m, inplace = True)
ma_m = df["Metascore"].mean() # mean of the matascore
df["Metascore"].fillna(ma_m, inplace=True)

#print(df.isnull().sum()) 
print("****The title of the movie with highest rating ******")
for ind in range(len(df['Rating'])):
    if df.iloc[[ind]]['Rating'].iat[0] ==  df['Rating'].max():
        #print(df.iloc[[ind]])
        print("")
        
        print("Title:", df.iloc[ind]['Title'])
        
        
        
        
print("")        
print("****The average revenue of all movies*****")
print(df["Revenue(Millions)"].sum()/len(df))
print("")

print("****The average revenue from 2015 to 2017****")
df15_17 = df[2015<=df['Year']] ## no movies after 2016
print(df15_17["Revenue(Millions)"].sum()/len(df15_17))
print("")

print("****Number of movies in 2016*****")
print(len(df[df["Year"] == 2016]))
print("") 

print("****Number of Movies Directed by Christopher Nolan*****")
df_CN = df[df["Director"] == "Christopher Nolan"]
print(df_CN )
print("Number of movies Driected by Nolan is:", len(df[df["Director"] == "Christopher Nolan"]))
print("")



print("****Number of Movies with Rating 8.0 and above*****")
df8 = df[8.0 <= df["Rating"]]

print(len(df8))
print("")

print("****Average Rating of movies Directed by Christopher Nolan*****")
print(df_CN['Rating'].median())
print("")


print("****the year with the highest average rating*****")

In2016 = df[df["Year"] == 2016]["Rating"].mean()
In2008 = df[df["Year"] == 2008]["Rating"].mean()
In2007 = df[df["Year"] == 2007]["Rating"].mean()
In2006 = df[df["Year"] == 2006]["Rating"].mean()
print("")

print("Rating in 2016:"); print(In2016)
print("Rating in 2008:")
print(In2008)
print("Rating in 2007:")
print(In2007)
print("Rating in 2006:")
print(In2006)
print("")

print("The rating maximum is:")
print(max(In2016, In2008, In2007, In2006))
print("")

print("*****The percentage increase in number of movies made between 2006 and 2016****")

l6 = len(df[df["Year"] == 2006])
l16 = len(df[df["Year"] == 2016])

print(100*((l16 - l6)/l6))    

print("")
print("******the most common actor in all the movies*******")
df_nsp = "[{}]".format(",".join(map(str, df["Actors"]))) # make Actors name list
df_nsp = df_nsp.replace(", ",",") #avoid spaces
print(pd.DataFrame(df_nsp.split(",")).value_counts())
print("The most common actor is:", pd.DataFrame(df_nsp.split(",")).value_counts().index[0])
print("Number of movies:", max(pd.DataFrame(df_nsp.split(",")).value_counts()))
print("")



print("******The number of unique genres*******")
df_ge = df["Genre"].str.split(",", expand=True)
df_geG = df_geG = pd.concat([df_ge[0], df_ge[1], df_ge[2]], axis=0, ignore_index=True)
print(len(df_geG.value_counts()))
print("")

print("****Corelation******")
#Numberial values only
df_n = df.drop(columns=["Title", "Genre", "Description", "Director", "Actors" ]).corr()
print(df_n)
#df_n.plot()
#plt.show()


