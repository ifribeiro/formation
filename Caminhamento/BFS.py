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

        self.fila = []

        #    G =  A  B  C  D  E  F  G  H
        self.G =[[0, 1, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 1],
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


    
    def busca_largura(self,v):
        for i in self.V:
            self.visitado[i] = False

        self.visitado[v] = True
        self.fila.append(v)
        while (len(self.fila)!=0):
            w = self.fila.pop(0)
            print (w)
            neighboors = self.neighboors([w])
            for i in neighboors:
                if(self.visitado[i]==False):
                    self.visitado[i] = True                    
                    self.fila.append(i)
    
    def gerarMatrizAdjacencia(self, V, E=None):
        matriz = np.zeros((len(V), len(V)))
        for i in range(0, len(V)):
            for j in range(0, len(V)):
                vertice1 = V[i]
                vertice2 = V[j]
                if((vertice1,vertice2) in E):
                    matriz[i,j] = 1
        
        print (matriz)

if __name__ == '__main__':
    busca = Caminhamento()
    E = [("A","B"),("A","C"),("B","A"),("C","A"), 
    ("B","D"), ("B","E"), ("C","F"), ("C","G"), ("D","B"),
    ("D","H"),("E","B"),("E","H"),("F","C"),("F","H"),("G","C"),
    ("H","D"),("H","E"),("H","F"),("H","G"),("G","H")]
    busca.gerarMatrizAdjacencia(V=busca.V,E=E)

        


