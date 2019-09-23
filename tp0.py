#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:12:05 2019

@author: gperez01
"""
from vect import *

for i in range (4):
    print (i)
    
for i in range (1,4):
    print (i)
    
for i in range (1,12,3):
    print (i)
    
    
G = [[], [2, 5, 5], [1, 3, 4, 4], [2, 3, 4], [2, 2, 3, 5], [1, 1, 4]]

print("nbAretes = ", nbAretes(G))

i = 2
print (G)
print (G[i])
print (G[i][i])

if 3 in G[2]:
    print ("true")
    
if 2 not in G[2]:
    print ("true")

print (3 in G[2])

M = initMat(2,1)
M[0][0]=4
print(M)