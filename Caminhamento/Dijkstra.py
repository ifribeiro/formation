#!/usr/bin/env python3

import numpy as np


class Dijkstra():
    def __init__(self):
        self.initVariables()
    
    def initVariables(self):
        anterior=[]
        self.V = [1,2,3,4,5,6]
        self.custos = np.array([            
            [0,10,5,np.Infinity,np.Infinity,np.Infinity],
            [10,0,4,1,4,np.Infinity],
            [5,4,0,np.Infinity,6,np.Infinity],
            [np.Infinity,1,np.Infinity,0, 2,3],
            [np.Infinity,4,6,2,0,1],
            [np.Infinity,np.Infinity,np.Infinity,3,1,0]
            ])
    def dijkstra(self, v):
        Vini = self.v(v)
        custos = np.zeros((6,6))
        for i in range(0,len(self.custos)):
            if(i != Vini):
                custos[Vini,i] = np.Infinity
            else:
                custos[Vini,i] = 0
        fechado = set({})
        aberto = set(self.V)
        anterior = np.zeros(len(self.V))
        
        k = self.getClosestVertice(v, aberto)
        fechado = fechado.union(set({k}))
        aberto  = aberto.difference(set({k}))
        #print aberto.intersection(self.neighboors())
        #anterior = np.zeros(len(V))
        #while (len(aberto)!= 0){
        #    k = 
        #}
        print (aberto.intersection(self.neighboors([k])))
        for i in (aberto.intersection(self.neighboors([k]))):
            if (Vini != self.v(i)):
                #print (Vini, self.v(i))
                custo = min(custos[Vini, self.v(i)], self.custos[Vini, self.v(k)]+self.custos[self.v(k), self.v(i)])
                if (custo < custos[Vini,self.v(i)]):
                    custos[Vini,self.v(i)] = custo
                    anterior[self.v(i)] = k
        
        print (anterior)

            

    """
    " V = set of Vertices
    " Returns = set of Neighboors of v
    """
    def neighboors(self,V):
        neighboors_vertices = set() # initializes vertices' array
        for i in V:            
            pos = self.v(i) # position of vertice in array        
            vertices = self.custos[pos] # adjacency of vertice v            
            for i in range(0,len(vertices)): 
                if(vertices[i]>0 and vertices[i]<np.Infinity):
                    neighboors_vertices.add(self.V[i])
        return neighboors_vertices
       

    def getClosestVertice(self, v, aberto):
        menor = np.Infinity
        closest = None
        for i in aberto:
            if (i != v):
                temp = self.custos[self.v(v),self.v(i)]
                if (temp<menor):
                    closest=i
                    menor = temp
                

        return closest
    
    def v(self, v):
        """
        Retorna o índice do vértice

        """
        return self.V.index(v)
    
if __name__ == '__main__':
    Dijkstra = Dijkstra()

    #print (Dijkstra.neighboors([4]))
    Dijkstra.dijkstra(1)
        
        