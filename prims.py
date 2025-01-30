INR = 9999999
V = 5
G = [[0, 2, 0, 6, 0],
     [2, 0, 3, 8, 5],
     [0, 3, 0, 0, 7],
     [6, 8, 0, 0, 0],
     [0, 5, 7, 0, 0]]

selected = [0, 0, 0, 0, 0]
no_edge = 0

selected[0] = True
print("Edge : Weight\n")
while (no_edge < V - 1):

    min = INR
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    if min > G[i][j]:
                        min = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1