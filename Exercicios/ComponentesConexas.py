import numpy as np
from Conex import Conex
grafos = []
nTestes = int(input())

vertices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','k','r','s','t','u','v','x','z','w']
print (vertices.index('a'))

for grafo in range(0,nTestes):
    print ("Vertice - Arestas")
    nVert_Ares = input().split(" ")
    print (nVert_Ares)
    matrix = np.zeros((int(nVert_Ares[0]), int(nVert_Ares[0])))
    grafos.append(matrix)

    for j in range(0, int(nVert_Ares[1])):
        print ("Vertice Vertice")
        conexao = input().split(" ")
        if (conexao[0] != ''):
            idx1 = vertices.index(conexao[0])
            idx2 = vertices.index(conexao[1])
            grafos[grafo][idx1][idx2] = 1
        else:
            grafos[grafo][idx1][idx2] = 0


c = Conex(grafos[0])
c.calcConex()



