

def existeCaminho(adj, vert, v, w):
    #print('V: {} W: {} OK: {}'.format(v, w, w in adj[v]))
    if w in adj[v]:
        return True

    vert[v] = 1
    for i in range(0, len(adj[v])):
        #print ('marca V: {} = {} '.format(adj[v][i], vert[adj[v][i]]))
        if vert[adj[v][i]] != 1:
            return existeCaminho(adj, vert, adj[v][i], w)

    return False


if __name__ == '__main__':

    while True:
        v, e = input().split(" ")
        v_, e_ = '', ''

        if int(v) == 0 and int(e) == 0:
            break
        vertices = {}
        adjacencias = {}

        for j in range(0, int(e)):
            v_, w_, p_  = input().split(" ")
            vertices[v_] = 0
            vertices[w_] = 0
        
            adjacencias.setdefault(v_, [])
            adjacencias.setdefault(w_, [])
            adjacencias[v_].append(w_)

            if int(p_) == 2:
                adjacencias[w_].append(v_)

        #print(adjacencias)
        para = False
        for i in vertices:
            for j in vertices:
                if i == j: continue
                vert = vertices.copy()
                #print ('V: {} W: {} = {}'.format(i, j, existeCaminho(adjacencias, vert, i, j)))
                vert = vertices.copy()
                if existeCaminho(adjacencias, vert, i, j) == False:
                    para = True
                    break
            if para: break
        if para:
            print('0')
        else:    
            print('1')   
