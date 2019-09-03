#!/usr/bin/env python3

import random
import numpy as np

class Conex():
    def __init__(self):

        self.initvariables() # inicializacao de variaveis


    def initvariables(self):
        self.V = ['a','b','c','d','e','f','g','h','i','j']
        self.R = {}
        #    G =  a  b  c  d  e  f  g  h  i  j
        self.G =[[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
                ]
        
        for i in self.V:
            self.R[i] = []

    def calcConex(self):
        vertice = random.randint(0,9)
        #v = V[i]
        v = 'a'
        self.R[v].append(v)
        Y = []
        #v = 'a'
        difference = (set(self.neighboors(v)) - set(self.R[v]))
        if (len(difference)==0):
            print ('empty')
        else:
            print ("not empty")

    """
    "v = Vertice
    "Returns = Neighboors of v
    """
    def neighboors(self,v):
        pos = self.returnIndex(v) # position of vertice in array        
        vertices = self.G[pos] # adjacency of vertice v
        neighboors_vertices = [] # initializes vertices' array
        for i in range(0,len(vertices)): 
            if(vertices[i]==1):
                neighboors_vertices.append(self.V[i])
        return neighboors_vertices

    def returnIndex(self, v):
        return self.V.index(v)
if __name__ == '__main__':
    Conex = Conex()
    print (Conex.calcConex())