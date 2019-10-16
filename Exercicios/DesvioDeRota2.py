import numpy as np
class Dijkstra():
    def __init__(self, custos, C, K):
        self.init_variable(custos,C,K)        
    def init_variable(self, custos,C,K):
        self.V = self.creatList(len(custos))
        self.custos = custos        
        self.C = C
        self.K = K
        self.rota = self.creatList(C)
    def creatList(self, n):
        list = []
        for i in range(0,n):
            list.append(i)
        return list
    def zeros(self, nColunas):
        M = []
        row = []
        for i in range(0,nColunas):
            row = []
            for j in range(0,nColunas):
                row.append(0)
            M.append(row)    
        return M
    def list_zeros(self,nColunas):
        list = []
        for i in range(0,nColunas):
            list.append(0)
        return list

    def dijkstra2(self,v):
        Vini = v
        d = self.zeros(len(self.V))
        for i in range(0,len(self.custos)):
            if(i != Vini):
                d[Vini][i] = 9223372036854775807
            else:
                d[Vini][i] = 0
        fechado = set({})
        aberto = set(self.V)
        anterior = self.list_zeros(len(self.V))        
        k = v
        while (len(aberto)!= 0):                     
            k = self.getClosestVertice(Vini, k, aberto, d,fechado)
            print ("closest ",k)
            vAtual = k            
            fechado = fechado.union(set({k}))
            aberto  = aberto.difference(set({k}))
            print ("aberto", aberto)     
            for i in (aberto.intersection(self.neighboors([k]))):                                            
                custo = min(d[Vini][i], d[Vini][k]+self.custos[k][i])
                print ("i", i)
                print ("min ", d[Vini][i], d[Vini][k]+self.custos[k][i])
                print ("custo:",custo)               
                if(vAtual in self.rota):
                    if((i==self.C-1) and (i-vAtual!=1)):
                        print ("Entrou aqui")                      
                        continue                         
                if (custo < d[Vini][i]):
                    d[Vini][i] = custo                    
                    anterior[i] = k
                
        #print (d[Vini])
        return d[Vini]      
               
    def neighboors(self,V):
        neighboors_vertices = set() # initializes vertices' array        
        for i in V:            
            pos = i # position of vertice in array 
            #print ("i = %s pos = %s" % (i, pos))
            vertices = self.custos[pos] # adjacency of vertice v            
            for i in range(0,len(vertices)): 
                if(vertices[i]>=0 and vertices[i]<9223372036854775807):
                    neighboors_vertices.add(self.V[i])
        return neighboors_vertices       

    def getClosestVertice(self, vini, v, aberto, custos, fechado):
        menor = 9223372036854775807
        #print ("V: ", v)
        #print ("aberto ", aberto)
        #print ("Fechado ",fechado)
        if (v in self.rota) and (v!=self.C-1):            
            closest = v+1
            if (closest not in fechado):
                #print (closest, "NOT IN FECHADO")
                return closest
        #print ("Aberto", aberto)
        rotas = aberto.intersection(set(self.rota)).intersection(self.neighboors([v]))     
                
        closest = None        
        if v in aberto:            
            closest = v
            return closest        
        else:
            for i in aberto:                  
                temp = custos[vini][i]                
                if (temp<menor):
                    closest=i
                    menor = temp

        #print ("Closest ",closest)
        return closest
    def nextInRoute(self,aberto):
        inroute = list(set(self.rota).intersection(aberto))
        return inroute
        

class Routes():
    def __init__(self):
        self.grafos = []
        self.C = []
        self.K = []
    def createRoutes(self):        
        while(True):
            NMCK = input()
            if (NMCK != "0 0 0 0"):
                N,M,C,K = NMCK.split(" ")
                self.C.append(int(C))
                self.K.append(int(K))                
                matrix = self.matrix_inf(int(N))
                for i in range(0, int(M)):
                    U,V,P = input().split(" ")                    
                    matrix[int(U)][int(V)] = int(P)
                    matrix[int(V)][int(U)] = int(P)
                #print ("Matrix ", matrix)
                self.grafos.append(matrix)

            else:
                break
    def matrix_inf(self,N):
        M = []
        row = []
        for i in range(0,N):
            row = []
            for j in range(0,N):
                row.append(9223372036854775807)
            M.append(row)
        return M

    def calculateRoutes(self):
        i = 0
        for grafos,C,K in zip(self.grafos,self.C, self.K):
            print (C,K)            
            dijkstra = Dijkstra(grafos,C,K)
            pedagios = dijkstra.dijkstra2(K)
            min = pedagios[C-1]
            i = i+1
            print ("%d"%(min))
if __name__ == "__main__":
    Routes = Routes()
    Routes.createRoutes()
    Routes.calculateRoutes()