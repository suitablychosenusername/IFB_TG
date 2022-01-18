from Graph_FabioLapa import Graph as gph

if __name__ == '__main__':
    # g1 = gph()
    # # Collabotarion graph:
    # g1.readInput('TG/Trabalho01_FabioLapa/collaboration_graph.txt')
    # # Imprime lista de adjacencia:
    # g1.writeList()
    # # # Salva a lista de adjacencia em um arquivo CSV:
    # g1.writeListCSV("TG/Trabalho01_FabioLapa/collaboration_adjacency_list.csv")
    # # # Escreve lista de componentes:
    # g1.componentList('TG/Trabalho01_FabioLapa/collaboration_componentlist.txt')

    # g1 = gph()
    # # lê apenas as primeiras 999 arestas e não preenche os vertices não declarados
    # g1.readInput('TG/Trabalho01_FabioLapa/collaboration_graph.txt', 999, False)
    # # # escreve matrix
    # g1.writeMatrix()
    # # # escreve matrix em arquivo csv
    # g1.writeMatrixCSV('TG/Trabalho01_FabioLapa/collaboration_adjacency_matrix.csv')

    # g1 = gph()
    # AS graph:
    # g1.readInput('TG/Trabalho01_FabioLapa/as_graph.txt')
    # Salva o arquivo de saída como solicitado.
    # g1.writeOutput('TG/Trabalho01_FabioLapa/as_output.txt')
    # Salva uma lista de componentes de as.
    # g1.componentList('TG/Trabalho01_FabioLapa/as_componentlist.txt')
    # Salva listas de BFS's partindo de 1, 32835 e 16192:
    # g1.search(1, 0, 'TG/Trabalho01_FabioLapa/as_searchWidth_v1.txt')
    # g1.search(32385, 0, 'TG/Trabalho01_FabioLapa/as_searchWidth_v32385.txt')
    # g1.search(16192, 0, 'TG/Trabalho01_FabioLapa/as_searchWidth_v16192.txt')
    # g1.search(42, 0, 'TG/Trabalho01_FabioLapa/as_searchWidth_v42_bfs.txt')
    # g1.search(42, 1, 'TG/Trabalho01_FabioLapa/as_searchWidth_v42_dfs.txt')
    # g1.lvlSearchWidth(1)
    # g1.lvlSearchWidth(32385)
    # g1.lvlSearchWidth(16192)
    # g1.lvlSearchWidth(42)
    # Imprime o diametro de g1
    # print(g1.findDiameter(42))

    g2 = gph()
    # g2.readInput("TG/input_wgt.txt")
    g2.readInput("TG/Trabalho01_FabioLapa/input1.txt")
    g2.writeOutput("TG/output_wgt.txt")
    g2.writeList()
    g2.writeListCSV("TG/output_wgt.CSV")
    g2.writeMatrix()
    g2.search(1, 0, "bfs.txt")
    g2.search(1, 1, "dfs43.txt")
    g2.findDiameter(1)
    g2.componentList("cp.txt")
    # distance, path = g2.dijkstra(1, 3)
    # print("Distance from 1 to 3 is:", distance, "\nShortest path is: ", end=" ")
    # for i in path:
    #     print(i, end=" ")
    # print()
    # distance, path = g2.dijkstra(1, 5)
    # print("Distance from 1 to 5 is:", distance, "\nShortest path is: ", end=" ")
    # for i in path:
    #     print(i, end=" ")
    # print()
    # distance, path = g2.dijkstra(1, 4)
    # print("Distance from 1 to 4 is:", distance, "\nShortest path is: ", end=" ")
    # for i in path:
    #     print(i, end=" ")
    # print()
    # distance, path = g2.dijkstra(1, 10)
    # print("Distance from 1 to 10 is:", distance, "\nShortest path is: ", end=" ")
    # for i in path:
    #     print(i, end=" ")
    # print()
    # distance, path = g2.dijkstra(1, 100)
    # print("Distance from 1 to 100 is:", distance, "\nShortest path is: ", end=" ")
    # for i in path:
    #     print(i, end=" ")
    # print()
    # distance, path = g2.dijkstra(1, 1000)
    # print("Distance from 1 to 1000 is:", distance, "\nShortest path is: ", end=" ")
    # for i in path:
    #     print(i, end=" ")
    # print()
    # distance, path = g2.dijkstra(1, 10000)
    # print("Distance from 1 to 10000 is:", distance, "\nShortest path is: ", end=" ")
    # for i in path:
    #     print(i, end=" ")
    # print()

    root = "TG/Trabalho02_FabioLapa/trab2grafo_"
    for i in range(1, 2):
        g1 = gph()
        aux = root + str(i) + ".txt"
        g1.readInput("TG/Trabalho01_FabioLapa/input1.txt")
        print('\nGrafo', i, "N =", g1.size)
        g1.dijkstra(1)
        dest = 1
        for k in range(1, 5):
            dest *= 10
            if dest > g1.size:
                break
            distance, path = g1.shortest_path(dest)
            print("Distance from 1 to", dest, "is:", distance, "\nShortest path is: ", end=" ")
            for j in path:
                print(j, end=" ")
            print()