## Install the Jellyfish library 
#!pip install jellyfish

## For data manipulation
from lib2to3.pgen2 import driver
import pandas as pd
from difflib import SequenceMatcher

## For numerical computations
import numpy as np

## For Visualizations
import seaborn as sns 
import matplotlib.pyplot as plt

## To calculate the Levenshtein distance.
import jellyfish

Adebola = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=1)
AM2021 = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=2)
AnnAnna = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=3)
Anuj = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=4)
Elbeth = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=5)
BFA = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=6)
Bobjiang = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=7)
Iamgold = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=8)
LKH = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=9)
Waka = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=10)
Tricelex = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=11)
OxProof = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=12)
Emmanel = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=13)
FizzyMidas = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=14)
Doggfather = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=15)
Flobisnitz = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=16)
EmmanuelJacobson = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=17)
Greg = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=18)
GreyTrainer = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=19)
Stelescuvlad = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=20)
CassCee = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=21)
Jshua = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=22)
Kishoraditya = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=23)
Kylin = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=24)
Z4yr0 = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=25)
TheHound = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=26)
MountManu = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=27)
Nadalie = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=28)
Richard = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=29)
Ogunsojosam = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=30)
AM2021 = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=31)
RobotTeddy = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=32)
AnnAnna2 = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=33)
Steegecs = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=34)
ViktorLiu = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=35)
Socal = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=36)
Wolfman = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=37)
ZER8 = pd.read_excel("./GR13_Human_Evaluation_-_FINAL.xlsx", sheet_name=38)

# Storing each reviewer dataset in a list, for easy iteration.
names = [Adebola, AM2021, Anuj, Elbeth, BFA, Iamgold, Bobjiang, LKH, FizzyMidas,Tricelex, OxProof,
         Emmanel, Doggfather, EmmanuelJacobson, Flobisnitz, Greg, GreyTrainer, Stelescuvlad,
         Jshua, Kylin, TheHound, MountManu, Nadalie, Richard, Ogunsojosam, RobotTeddy,
         AnnAnna, Socal, Steegecs, ViktorLiu, Wolfman, ZER8, Kishoraditya, AnnAnna2, Waka, CassCee ]

# Making a loop through all the datasheet of human evaluation,
# then renaming the Unnamed: 0 column to handle so that all the data used for the analysis have a column in common
for i in names:
    i.rename({"Unnamed: 0": "handle"}, axis=1, inplace=True)

## Concatenating all the available datasets for this round (1).
concat_data = pd.concat(names)

## Dropping duplicated handles.
concat_data.drop_duplicates(subset=["handle"], inplace=True)

## Calculating the distances 
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:56:48 2022

@author: Ogunjo Samuel
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 09:47:59 2022

@author: Ogunjo Samuel
"""

## I limited the handles to the first 1000. You can remove the [:1000] to run it on all the 1432 handles.
x = concat_data["handle"][:1000]

y = x.unique()

## This creates a zero matrix shaped len of x (1000) X len of x(1000)
alpha0 = np.zeros((len(x),len(x)))
k = 0; g = 0;
## This loop calculates the Levenshtein distance of all the handles.
for ii,i in enumerate(y):
    
    for jj, j in enumerate(x):
        
        s = jellyfish.levenshtein_distance(i,j)
        
        #print(s)
        alpha0[ii][jj] = s
            
        #k = k + 1; g = g + 1

#fig, ax = plt.subplots(figsize=(25,10))

## This creates the dataframe showing the Levenshtein distance of any pair of handles.
Ld = pd.DataFrame(alpha0,columns=x,index=x)
#hz = hy[hy > 0.4].dropna(axis=1,how='all')
#sns.heatmap(hy, annot=True)

## To get the mean distance of each handle across the others
ld_avg = pd.DataFrame()
ld_avg["handles"] = Ld.iloc[:, :].mean().index
ld_avg["Average"] = Ld.iloc[:, :].mean().values

## To generate the list for Account 1| Account 2| Distance

distances = []
userss = []
for name in concat_data["handle"][:1000]:
    x = concat_data["handle"][:1000]

    y = [name]

    ## This creates a zero matrix shaped len of x (1000) X len of x(1000)
    alpha0 = np.zeros(len(x))
    k = 0; g = 0;
    ## This loop calculates the Levenshtein distance of all the handles.
    for ii,i in enumerate(y):
        

        for jj, j in enumerate(x):
            userss.append(j)

            s = jellyfish.levenshtein_distance(i,j)

            #print(s)
            alpha0[jj] = s
    
    distances.append(alpha0)

## Creating the dataframes as below;
distance = []
for i in range(1000):
    distance.extend(distances[i])


handless = []
for i in concat_data["handle"][:1000]:
    handless.append([i] * 1000)

list_ = []
for i in range(1000):
    list_.extend(handless[i])

df = pd.DataFrame()
df["Account 1"] = list_
df["account 2"] = userss
df["Distance"] = distance


# Sorting the data
df.sort_values(by="Distance", inplace=True)
# To remove the rows where account1 and account2 are the samething
dff = df[1000:]

## Resetting the index after removing the first 1000 rows
dff.reset_index(drop=True, inplace=True)
## Saving the data
dff.to_csv("Levenshtein_distance.csv", index=False)