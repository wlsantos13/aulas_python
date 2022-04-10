matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

matrix2 = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
]

matrix3 = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
]




def contar_rios(grafos, x=0, y=0, visitados=list()):
    rios = []
    for x in range(len(grafos)):
        for y in range(len(grafos[x])):
            if [x, y] not in visitados:
                rio = 0
                if grafos[x][y] == 1:
                    i = x
                    z = y
                    while i <= len(grafos) -1 and grafos[i][z] != 0:
                        if grafos[i][z] == 1 and [i, z] not in visitados:
                            visitados.append([i, z])
                            rio += 1
                        i += 1
                    i -= 1
                    while z < len(grafos[0]) and grafos[i][z] != 0:
                        if grafos[i][z] == 1 and [i, z] not in visitados:
                            visitados.append([i, z])
                            rio +=1
                        z += 1
                    z -= 1
                    while z >= 0 and grafos[i][z] != 0:
                        if grafos[i][z] == 1 and [i, z] not in visitados:
                            visitados.append([i, z])
                            rio +=1
                        z -= 1
                    z +=1
                    while i >= 0 and grafos[i][z] != 0:
                        if grafos[i][z] == 1 and [i, z] not in visitados:
                            visitados.append([i, z])
                            rio +=1
                        i -=1
                            
                            
                    rios.append(rio)
    return rios               

print(contar_rios(matrix))


