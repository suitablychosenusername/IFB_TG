from Graph_FabioLapa import Graph as gph

if __name__ == '__main__':

    root = "TG/Trabalho02_FabioLapa/trab2grafo_"
    for i in range(1, 6):
        g1 = gph(1)
        aux = root + str(i) + ".txt"
        g1.readInput(aux)
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
    # g1 = gph()
    # g1.readInput("TG/Trabalho02_FabioLapa/input.txt", fill_Isolated=False)
    # g1.search('g', 0, "out.txt")
    # print(g1.findDiameter('a'))