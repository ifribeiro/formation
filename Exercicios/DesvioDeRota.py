import numpy as np

class Dijkstra():
    def __init__(self, G):
        self.G = G    
    """
    def dijkstra(self, v):
        Vini = self.v(v)        
        d = np.zeros((6,6))
        for i in range(0,len(self.custos)):
            if(i != Vini):
                d[Vini,i] = np.Infinity
            else:
                d[Vini,i] = 0
        fechado = set({})
        aberto = set(self.V)
        anterior = np.zeros(len(self.V))        
        k = v        
        print ("custos: ", d[Vini])
        while (len(aberto)!= 0):            
            k = self.getClosestVertice(Vini, k, aberto, d)
            print ("closest: ",k)
            fechado = fechado.union(set({k}))
            aberto  = aberto.difference(set({k}))
            print ("fechado ",fechado)
            print ("Aberto ", aberto)            
            for i in (aberto.intersection(self.neighboors([k]))):                
                custo = min(d[Vini, self.v(i)], d[Vini, self.v(k)]+self.custos[self.v(k), self.v(i)])
                if (custo < d[Vini,self.v(i)]):                    
                    d[Vini,self.v(i)] = custo
                    anterior[self.v(i)] = k        
        print ("custos: ", d[Vini])"""

         
    """
    " V = set of Vertices
    " Returns = set of Neighboors of v
    
    def neighboors(self,V):
        neighboors_vertices = set() # initializes vertices' array        
        for i in V:            
            pos = self.v(i) # position of vertice in array 
            #print ("i = %s pos = %s" % (i, pos))
            vertices = self.custos[pos] # adjacency of vertice v            
            for i in range(0,len(vertices)): 
                if(vertices[i]>0 and vertices[i]<np.Infinity):
                    neighboors_vertices.add(self.V[i])
        return neighboors_vertices
       

    def getClosestVertice(self, vini, v, aberto, custos):
        menor = np.Infinity
        closest = None
        print (min(custos[vini]))
        for i in aberto:                       
            if (self.v(i)==self.v(v)):                          
                closest = v
                return closest 
            else:                            
                temp = custos[vini,self.v(i)]                
                if (temp<menor):
                    closest=i
                    menor = temp
        return closest
    
    def v(self, v):        
        return self.V.index(v)"""

class Routes():
    def __init__(self):
        self.grafos = []
    
    def createRoutes(self):
        
        while(True):
            NMCK = input()
            if (NMCK != "0 0 0 0"):
                N,M,C,K = NMCK.split(" ")
                matrix = np.inf*np.ones((int(N),int(N)))
                for i in range(0, int(M)):
                    U,V,P = input().split(" ")
                    matrix[int(U)][int(V)] = P
                    matrix[int(V)][int(U)] = P
                    print (matrix)                         
                
            else:
                break

    
if __name__ == "__main__":
    Routes = Routes()
    Routes.createRoutes()

        


