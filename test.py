#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:30:24 2019

@author: gperez01
"""

from nbSommets import *
from nbAretes import *
from ajoutArete import *
from enleveArete import *
from deg import *


G = [[], [2, 5, 5], [1, 3, 4, 4], [2, 3, 4], [2, 2, 3, 5], [1, 1, 4]]
print("G = ",G)

print ("nbSommets = ", nbSommets(G))
print("nbAretes = ", nbAretes(G))

ajoutArete(G,3,5)
print("ajoutArete(G,3,5) : ", G)

enleveArete(G,3,5)
print("enleveArete(G,3,5) : ", G)

print("degré du sommet 2 = ", deg(G,2))