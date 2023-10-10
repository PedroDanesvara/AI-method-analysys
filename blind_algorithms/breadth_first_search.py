m_d = {
    0: 'Arad', 1: 'Zerind', 2: 'Timisoara',
    3: 'Oradea', 4: 'Lugoj', 5: 'Sibiu',
    6: 'Mehadia', 7: 'Fagaras', 8: 'Rimnicu Vilcea',
    9: 'Dobreta', 10: 'Bucharest', 11: 'Pitesti',
    12: 'Craiova', 13: 'Giurgiu', 14: 'Urziceni',
    15: 'Vaslui', 16: 'Hirsova', 17: 'Iasi',
    18: 'Eforie', 19: 'Neamt'}

fork = [[1, 2, 5],   
        [0, 3],  
        [0, 4],   
        [1, 5],   
        [2, 6],   
        [0, 3, 7, 8],   
        [4, 9],   
        [5, 10],   
        [5, 11, 12],   
        [6, 12],   
        [7, 11, 13, 14],   
        [8, 10, 12],   
        [8, 9, 11],     
        [10],   
        [10, 15, 16],   
        [14, 17],   
        [14, 18],   
        [15, 19],   
        [16],   
        [17]]   


first_node = 0
last_node = 10
visited_nodes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def breadthFirstSearch(first_node, last_node):
    fila = []
    fila.append(first_node)
    while len(fila) > 0:
        node = fila.pop(0)
        visited_nodes[node] = 1
        print(m_d[node])

        if node == last_node:
            print("Chegou ao destino")
            break
        for index in fork[node]:
            if visited_nodes[index] == 0:
                visited_nodes[index] = 1
                fila.append(index)

breadthFirstSearch(first_node, last_node)
