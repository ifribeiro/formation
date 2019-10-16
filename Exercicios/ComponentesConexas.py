import random
from random import choice
import string

class Conex():
    def __init__(self, G):
        self.initvariables(G) # inicializacao de variaveis


    def initvariables(self, G):
        self.V_temp = list(string.ascii_lowercase)[:len(G)]
        self.V = set(self.V_temp)
        self.R = {}
        self.G = G
        
        for i in self.V:
            self.R[i] = set()
        self.conexComponet = []

    """
    " Return the conex components of a graph
    """
    def calcConex(self):

        #chooses a vertice of V
        v = choice(list(self.V))
        

        #add vertice v to dict R, with key 'v'
        self.R[v].add(v)
        
        #initialize Y as a set
        Y = set()

        #while there's a neighboor vertice
        while(len(self.neighboors(self.R[v]) - self.R[v])!=0):           
            
            #Calculate the neighboors of R(v) - R(v)
            Y = self.neighboors(self.R[v]) - self.R[v]

            #R(v) = R(v) U Y
            self.R[v] = self.R[v] | Y

            #add R(V) to array conexComponent
            #Garante que apenas o maximal será adicionado            
            for set_vertices in self.conexComponet:                
                if (len(set_vertices)<len(list(self.R[v]))):                
                    if(all([x in list(self.R[v]) for x in set_vertices ])):
                        self.conexComponet.remove(set_vertices)                   
            
            
        self.conexComponet.append(list(self.R[v]))
        #set as R(v)
        Y = self.R[v]
        

        #set V as the difference between the sets V and Y
        self.V = self.V - Y        
        #if there's vertices left in V
        if (len(self.V)!=0):
            self.calcConex()
        
        return self.conexComponet
        

    """
    " V = set of Vertices
    " Returns = set of Neighboors of v
    """
    def neighboors(self,V):
        neighboors_vertices = set() # initializes vertices' array
        for i in V:            
            pos = self.V_temp.index(i) # position of vertice in array
            neighboors_vertices.add(self.V_temp[pos]) #adiciona o próprio vertice na lista de vizinhos
            vertices = self.G[pos] # adjacency of vertice v            
            for i in range(0,len(vertices)): 
                if(vertices[i]==1):
                    neighboors_vertices.add(self.V_temp[i])
        return neighboors_vertices

class ConnectedComponents():
    def __init__(self):
        self.grafos = []
        self.vertices = list(string.ascii_lowercase)

    def createMatrices(self, nTestes):
        for grafo in range(0,nTestes):
            nVert_Ares = input().split(" ")    
            matrix = self.zeros(int(nVert_Ares[0]))
            self.grafos.append(matrix)
            for j in range(0, int(nVert_Ares[1])):
                conexao = input().split(" ")
                if (conexao[0] != ''):
                    idx1 = self.vertices.index(conexao[0])
                    idx2 = self.vertices.index(conexao[1])
                    self.grafos[grafo][idx1][idx2] = 1
                    self.grafos[grafo][idx2][idx1] = 1
                else:
                    self.grafos[grafo][idx1][idx2] = 0

    def zeros(self, nColunas):
        M = []
        row = []
        for i in range(0,nColunas):
            row = []
            for j in range(0,nColunas):
                row.append(0)
            M.append(row)
        return M

    def calcConnectedComponents(self):
        for i in range(0,len(self.grafos)):
            print ("Case #%s:"%(i+1))
            c = Conex(self.grafos[i])
            listConex = (c.calcConex()) #ordena as componentes conexas
            listConex = [sorted(x) for x in listConex]
            listConex = sorted(listConex)
            for component in listConex:
                component = sorted(component)
                print (",".join(component)+",")
            print ("%s connected components\n"%(len(listConex)))
    
if __name__ == "__main__":
    CC = ConnectedComponents()
    nTestes = int(input())
    CC.createMatrices(nTestes)    
    CC.calcConnectedComponents()