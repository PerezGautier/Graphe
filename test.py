#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:30:24 2019

@author: gperez01
"""

from TP1 import *
from vect import *

def nonOriente(M):
    for i in range(len(M)):
        for j in range(len(M)):
            if (M[i][j] != M[j][i]):
                return "false"
    return "true"

def kuratowski(n):
    G=[[]]
    for i in range(1,n+1):
        L=[]
        for j in range (1,n+1):
            if (i!=j):
                L.append(j)
        G.append(L)
    return G

def ListeToMatrice(G):
    n = len(G)-1
    #print("longueur de G = ",n)
    M = initMat(n,0)
    for i in range(n):
        #print ("i = ",i)
        for j in range(n):
            #print("j = ",j)
            if j+1 in G[i+1]:
                #print("M[",i-1,"][",j-1,"]")
                M[i][j]=1
    return M

G = [[], [2, 5, 5], [1, 3, 4, 4], [2, 3, 4], [2, 2, 3, 5], [1, 1, 4]]
print("G = ",G)
"""
M = initMat(5,0)

M[0][1]=1
M[0][4]=2
M[1][0]=1
M[1][2]=1
M[1][3]=2
M[2][1]=1
M[2][2]=1
M[2][3]=1
M[3][1]=2
M[3][2]=1
M[3][4]=1
M[4][0]=2
M[4][3]=1
affMat(M)
print(nonOriente(M))
D=kuratowski(5)
print(D)
"""
M=ListeToMatrice(G)
affMat(M)

"""
print ("nbSommets = ", nbSommets(G))
print("nbAretes = ", nbAretes(G))

ajoutArete(G,3,5)
print("ajoutArete(G,3,5) : ", G)

enleveArete(G,3,5)
print("enleveArete(G,3,5) : ", G)

print("degré du sommet 2 = ", deg(G,2))
"""