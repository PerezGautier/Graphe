# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:22:56 2019

@author: Gauti
"""

def nbSommets(G):
    return len(G)-1

def nbAretes(G):
    nb = 0
    for i in range(1, len(G)):
        nb = nb + len(G[i])
        if i in G[i]:
            nb = nb +1
    return nb/2

def ajoutArete(G,i,j):
    G[i].append(j)
    G[j].append(i)
    
    
def enleveArete(G,i,j):
    if j in G[i]:
        G[i].remove(j)
    if i in G[j]:
        G[j].remove(i)
        
def deg(G,i):
    return len(G[i])

def degre(G):
    D = []
    for i in range(1, len(G)):
        D.append(deg(G,i))
    return D

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
    M = initMat(n,0)
    for i in range(n):
        for j in range(n):
            if j+1 in G[i+1]:
                M[i][j]=1
    return M