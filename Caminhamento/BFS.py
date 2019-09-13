#!/usr/bin/env python3

import random
from random import choice
import numpy as np

class Caminhamento():
    def __init__(self):
        self.initvariables() # inicializacao de variaveis
    def initvariables(self):
        self.V = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.visitado = {}

        #    G =  A  B  C  D  E  F  G  H
        self.G =[[0, 1, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 1, 1, 1, 0]
                ]

    def busca_prof(self):
        for i in self.V:
            self.visitado[i] = False
        for i in self.V:
            if (self.visitado[i]==False):
                print (i)
                self.prof(i)
    
    def prof(self, v):
        
        self.visitado[v] = True        
        print (v)
        neighboors = self.neighboors([v])
        for w in neighboors:
            if (self.visitado[w]==False):
                self.prof(w)
    
    """
    " V = set of Vertices
    " Returns = set of Neighboors of v
    """
    def neighboors(self,V):
        neighboors_vertices = set() # initializes vertices' array
        for i in V:            
            pos = self.V.index(i) # position of vertice in array        
            vertices = self.G[pos] # adjacency of vertice v            
            for i in range(0,len(vertices)): 
                if(vertices[i]==1):
                    neighboors_vertices.add(self.V[i])
        return neighboors_vertices
if __name__ == '__main__':
    busca = Caminhamento()
    busca.busca_prof()

        


