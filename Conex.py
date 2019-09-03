#!/usr/bin/env python3

import random
from random import choice
import numpy as np


class Conex():
    def __init__(self):

        self.initvariables() # inicializacao de variaveis


    def initvariables(self):
        self.V_temp = ['a','b','c','d','e','f','g','h','i','j']
        self.V = set(['a','b','c','d','e','f','g','h','i','j'])
        self.R = {}
        #    G =  a  b  c  d  e  f  g  h  i  j
        self.G =[[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
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
            self.R[i] = set()

    def calcConex(self):
        v = choice(list(self.V))
        print('v: ', v)
        self.R[v].add(v)
        Y = set()
        
        #v = 'a'
        while(len(self.neighboors(self.R[v]) - self.R[v])!=0):
            Y = self.neighboors(self.R[v]) - self.R[v]
            self.R[v] = self.R[v] | Y
        
        Y = self.R[v]
        self.V = self.V - Y
        print ("V: ", self.V)

        """
        if (len(self.V)!=0){
            self.calcConex()
        }"""

    """
    "v = Vertice
    "Returns = set of Neighboors of v
    """
    def neighboors(self,v):
        neighboors_vertices = set() # initializes vertices' array
        for i in v:            
            pos = self.returnIndex(i) # position of vertice in array        
            vertices = self.G[pos] # adjacency of vertice v            
            for i in range(0,len(vertices)): 
                if(vertices[i]==1):
                    neighboors_vertices.add(self.V_temp[i])
        return neighboors_vertices

    def returnIndex(self, v):
        return self.V_temp.index(v)
if __name__ == '__main__':
    Conex = Conex()
    print (Conex.calcConex())