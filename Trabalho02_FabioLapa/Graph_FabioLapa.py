import matplotlib as plt
from collections import defaultdict as ddict, OrderedDict as od
from queue import Queue as queue, LifoQueue as stack
import csv, os, heapq

class Ordering:
    def __init__(self, val=0, distance=0, parent='R', visited=False):
        self.val = val
        self.distance = distance
        self.parent = parent
        self.visited = visited
    
    def __eq__(self, rhs):
        return self.distance == rhs.distance
    
    def __lt__(self, rhs):
        if (self.visited):
            return rhs
        return self.distance < rhs.distance

class Vertex:
    def __init__(self, val=0, parent='R', level=0):
        self.val = val
        self.parent = parent
        self.level = level
    
    def __eq__(self, rhs):
        if type(rhs) is int:
            return self.val == rhs
        else:
            return self.val == rhs.val

    # def __eq__(self, rhs):

    def __str__(self) -> str:
        return str(self.parent) + " " + str(self.val) + " " + str(self.level)

class Graph:
    '''
    Class for implementing various Graph functions asked in Task01.
    '''
    def __init__(self, weighted=False):
        if weighted == False:
            self.edges = ddict(list)
        else:
            self.edges = ddict(dict)
        self.size = 0
        self.weighted = weighted
        self.isDijkstraPossible = True
        self.distance = ddict(list)

    def readInput(self, inputpath: str="input.txt",limit=-1, fill_Isolated=True):
        '''
        Reads an input file. Input path should be passed as argument.
        
        → inputpath: path to the file.
        → limit: limit of lines to read, aside the first line. Default will read all lines.
        → fill_Isolated: boolean to decide wheather or not to add isolated (undeclared) vertexes to the list of vertexes
            of the graph. Default will fill them in.
        '''

        if os.path.exists(inputpath):
            f = open(inputpath, 'r')
            self.size = int(f.readline().strip("\n"))
    
            lines = limit
            if self.weighted == False:
                for i in f:
                    if lines == 0:
                        break
                    stri, aux = i.strip("\n").split(" ")
                    if int(stri) not in self.edges[int(aux)]:
                        self.edges[int(aux)].append(int(stri))
                    if int(aux) not in self.edges[int(stri)]:
                        self.edges[int(stri)].append(int(aux))
                    if lines > 0:
                        lines -=1

            else:
                for i in f:
                    if lines == 0:
                        break
                    stri, aux, weight = i.strip("\n").split(" ")
                    if float(weight) < 0:
                        self.isDijkstraPossible = False
                    if not int(stri) in self.edges[int(aux)]:
                        self.edges[int(aux)][int(stri)] = float(weight)
                    if not int(aux) in self.edges[int(stri)]:
                        self.edges[int(stri)][int(aux)] = float(weight)
                    if lines > 0:
                        lines -=1

            if(fill_Isolated):
                for i in range(1, self.size+1):
                    if i not in self.edges:
                        self.edges[i] = []

            self.edges = od(sorted(self.edges.items()))

            if self.weighted == False:
                for i in self.edges:
                    self.edges[i].sort()
            else:
                for i in self.edges:
                    self.edges[i] = od(sorted(self.edges[i].items()))

            f.close()
            


        else:
            print("File not found.")


    def writeOutput(self, outputpath:str='output.txt'):
        '''
        Writes the output file.
        
        → outputpath: Path and name of the file to be written (i.e.: "my_workspace/output.txt")
        '''
        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return
        sum = 0
        f = open(outputpath, "w")
        big_degree = 0
        sml_degree = 999999
        # writes number of vertexes
        f.write("# n = " + str(self.size) + "\n")

        # sums the total of edges
        for i in self.edges:
            degree = len(self.edges[i])
            if degree < sml_degree:
                sml_degree = degree
            if degree > big_degree:
                big_degree = degree
            sum += degree

        # tests if graph is possible
        if sum % 2 != 0:
            f.write("impossible graph! - Odd number of edges!\n")
            # f.close()
            # return
        else:
            f.write("# m = " + str(int(sum/2)) + "\n")

        for i in self.edges:
            f.write(str(i) + " " + str(len(self.edges[i])) + "\n")
        f.close()
        print("maior grau: "+str(big_degree)+" menor grau: "+str(sml_degree))

    def writeList(self):
        '''
        Prints adjacency lists.
        '''
        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return
        
        if self.weighted == False:
            for i in self.edges:
                row = "[ " + str(i) + " ] -> "
                for j in self.edges[i]:
                    row += str(j) + " -> "
                print(row + "NULL")
        else:
            for i in self.edges:
                row = "[" + str(i) + " ] - > "
                for j in self.edges[i]:
                    row += "(" + str(j) + ", " + str(self.edges[i][j]) + ") -> "
                print(row + 'NULL')

    
    def writeListCSV(self, outputpath:str="listMatrix.csv"):
        '''
        Saves the adjacency matrix into a CSV file.

        → outputpath: relative (from workspace) or absolute path to output csv file.
            i.e.: "matrix.csv"
                  "/usr/home/my_workspace/Graphs/adjacency_matrix.csv"
        '''

        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return

        f = open(outputpath, "w", newline="")
        wrt = csv.writer(f)
        header = ["Vertex", "Neighbors"]
        wrt.writerow(header)
        
        if self.weighted == False:
            for i in self.edges:
                row = [str(i), "->"]
                for j in self.edges[i]:
                    row.append(str(j))
                    row.append("->")
                row.append("NULL")
                wrt.writerow(row)
        else:
            for i in self.edges:
                row = [str(i), "->"]
                for j in self.edges[i]:
                    row.append("(" + str(j) + ", " + str(self.edges[i][j]) + ")")
                    row.append("->")
                row.append("NULL")
                wrt.writerow(row)

        f.close()


    def writeMatrix(self):
        '''
        Prints adjacency matrix.
        '''
        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return
        if self.weighted == False:
            header = [" "] + list(self.edges)
            for i in header:
                print(i, end=" ")
            print()

            for i in self.edges:
                print(str(i), end=" ")
                for j in self.edges:
                    if j in self.edges[i]:
                        print(str(1), end=" ")
                    else:
                        print(str(0), end=" ")
                print()
        
        else:
            header = list(self.edges)
            print("  ", end="")
            for i in header:
                print("{0:<6}".format(i), end=" ")
            print()
            for i in self.edges:
                print(str(i), end=" ")
                for j in self.edges:
                    if j in self.edges[i]:
                        print("{0:<6}".format(self.edges[i][j]), end=" ")
                    else:
                        print("{0:<6}".format(0), end=" ")
                print()
    

    def writeMatrixCSV(self, outputpath:str="matrix.csv"):
        '''
        Saves the adjacency matrix into a CSV file.

        → outputpath: relative (from workspace) or absolute path to output csv file.
            i.e.: "matrix.csv"
                  "/usr/home/my_workspace/Graphs/adjacency_matrix.csv"
        '''

        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return

        f = open(outputpath, "w", newline="")
        wrt = csv.writer(f)

        if self.weighted == False:
            header = [" "] + list(self.edges)
            wrt.writerow(header)
            for i in self.edges:
                row = [str(i)]
                for j in self.edges:
                    if j in self.edges[i]:
                        row.append(str(1))
                    else:
                        row.append(str(0))
                wrt.writerow(row)
        else:
            header = [" "] + list(self.edges)
            wrt.writerow(header)
            for i in self.edges:
                row = [str(i)]
                for j in self.edges:
                    if j in self.edges[i]:
                        row.append(str(self.edges[i][j]))
                    else:
                        row.append(str(0))
                wrt.writerow(row)
        
        f.close()


    def searchWidth(self, x, outputpath):
        # abre arquivo
        f = open(outputpath, "w")

        # escreve header (P = Parent, V = Vertex, L = Level, W = Peso)
        if self.weighted == False:
            f.write("P V L\n")
        else:
            f.write("P V L W\n")

        q = queue(maxsize=0)
        visited = []
        edgesCopy = self.edges.copy()
        v = Vertex(x)
        q.put(v)
        max_lvl = 0

        while len(visited) < self.size:
            # Testa se a fila esta vazia. Se sim, encerra a busca
            if q.empty():
                break
            # Senao puxa o proximo da fila
            v = q.get()
            if v.level > max_lvl:
                max_lvl = v.level
            # marca elemento como visitado
            visited.append(v.val)

            # escreve vertice no arquivo
            if self.weighted == False:
                f.write(str(v)+"\n")
            elif v.parent != "R":
                f.write(str(v)+" "+ str(self.edges[v.parent][v.val]) + "\n")
            else:
                f.write(str(v)+"\n")
            
            # percorre lista de arestas de v
            for j in edgesCopy[v.val]:
                # coloca na fila se ja nao estiver e se nao tiver sido visitado
                if j not in visited and j not in q.queue:
                    aux = Vertex(j, v.val, v.level+1)
                    q.put(aux)
            
            edgesCopy.pop(v.val) # remove vertice para ficar mais facil buscar por grafos desconexos
        
        f.close()


    def lvlSearchWidth(self, x):
        q = queue(maxsize=0)
        visited = []
        edgesCopy = self.edges.copy()
        v = Vertex(x)
        q.put(v)
        max_lvl = 0

        while len(visited) < self.size:
            # Testa se a fila esta vazia. Se sim, encerra a busca
            if q.empty():
                break
            # Senao puxa o proximo da fila
            v = q.get()
            # if v.level > max_lvl:
                # max_lvl = v.level
            # marca elemento como visitado
            visited.append(v.val)
            
            # percorre lista de arestas de v
            for j in edgesCopy[v.val]:
                # coloca na fila se ja nao estiver e se nao tiver sido visitado
                if j not in visited and j not in q.queue:
                    aux = Vertex(j, v.val, v.level+1)
                    q.put(aux)
            
            edgesCopy.pop(v.val) # remove vertice para ficar mais facil buscar por grafos desconexos

        # print("vertex "+str(x)+" max lvl: "+str(max_lvl))
        return v


    def searchDepth(self, x, outputpath):
        # abre arquivo
        f = open(outputpath, "w")
        
        # escreve header (P = Parent, V = Vertex, L = Level)
        if not self.weighted:
            f.write("P V L\n")
        else:
            f.write("P V L W\n")

        visited = []
        s = stack()
        edgesCopy = self.edges.copy()
        if self.weighted:
            for i in self.edges:
                edgesCopy[i] = self.edges[i].copy()
        v = Vertex(x)
        s.put(v)

        # busca até visitar todos os nós possiveis
        while len(visited) < self.size:
            # se stack estiver vazia, encerra a busca
            if s.empty():
                break
            # verificador de vertice novo
            new = False

            # puxa o topo da stack
            v = s.queue[len(s.queue)-1]

            # se nao tiver sido visitado, marca como visitado e escreve no arquivo
            if v.val not in visited:
                visited.append(v.val)
                if self.weighted == False:
                    f.write(str(v)+"\n")
                elif v.parent != "R":
                    f.write(str(v)+" "+ str(self.edges[v.val][v.parent]) + "\n")
                else:
                    f.write(str(v)+"\n")

            # procura o "menor" vertice filho nao-visitado
            # for j in self.edges.keys():
            if self.weighted:
                while len(edgesCopy[v.val]) > 0:
                    if list(edgesCopy[v.val])[0] not in visited:
                        aux = Vertex(list(edgesCopy[v.val])[0], v.val, v.level+1)
                        s.put(aux)
                        edgesCopy[v.val].popitem(list(edgesCopy[v.val])[0])
                        new = True
                        break
                    edgesCopy[v.val].pop(list(edgesCopy[v.val])[0])
            else:
                while len(edgesCopy[v.val]) > 0:
                    if list(edgesCopy[v.val])[0] not in visited:
                        aux = Vertex(list(edgesCopy[v.val])[0], v.val, v.level+1)
                        s.put(aux)
                        edgesCopy[v.val].pop(0)
                        new = True
                        break
                    edgesCopy[v.val].pop(0)
            
            # se nao tiver encontrado nenhum filho nao-visitado, remove da pilha para retornar para o pai do atual
            if(new == False):
                s.get()
        f.close()


    def search(self, start, mode=None, outputpath: str=None) -> None:
        '''
        Saves a list of vertexes starting from start.

        → start: initial vertex.
        → mode: defines how the search shall be done.
            → 0: Width search.
            → 1: Depth search.
        → outputpath: The desired file name or the absolute path to it.
            → Default names should be "BFSTree.txt" or "DFSTree.txt", depending on which mode was selected.
        '''
        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return
        if mode == None:
            print('Please, define which mode to use.')
            return
        if outputpath == None:
            if mode == 0:
                outputpath = "BFSTree.txt"
            else:
                outputpath = "DFSTree.txt"
        if mode == 0:
            self.searchWidth(int(start), outputpath)
        else:
            self.searchDepth(int(start), outputpath)

    def findDiameter(self, x=None) -> int:
        '''
        Returns the highest minimum path of the graph.
        '''
        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return
        # edgesCopy = self.edges.copy()
        max_lvl = 0
        repeat = True
        if x == None:
            lvl = Vertex(list(self.edges)[0])
        else:
            lvl = Vertex(x)

        while repeat == True:
            repeat = False
            lvl = self.lvlSearchWidth(int(lvl.val))
            if lvl.level > max_lvl:
                max_lvl = lvl.level
                repeat = True

        return max_lvl


    def componentList(self, outputpath:str='componentlist.txt'):
        '''
        Saves a file with the list of components.

        → outputpath: The desired file name or the absolute path to it.
        '''
        if self.size == 0:
            print("There are no vertexes in this Graph.")
            return
        f = open("temporaryAndUselessButYetVeryUsefulFileThatNoOneShallKnowAboutItsExistence.txt", "w")
        comp = 1
        f.write("\n")
        q = queue(maxsize=0)
        visited = []
        component = []
        big_comp = 0
        sml_comp = 99999999
        edgesCopy = self.edges.copy()
        v = Vertex(list(edgesCopy.keys())[0])
        q.put(v)
        n_single = 0
        component_size = 0

        while len(visited) < self.size:
            # Testa se a fila esta vazia. Se sim, puxa o proximo elemento não-visitado
            if q.empty():
                f.write("\nComponente "+str(comp)+":\n")
                f.write("Tamanho: "+str(len(component))+"\n")
                component_size = len(component)
                if component_size == 1:
                    n_single += 1
                if component_size < sml_comp:
                    sml_comp = component_size
                if component_size > big_comp:
                    big_comp = component_size
                while len(component) > 0:
                    f.write(str(component.pop(0))+"\n")
                aux = Vertex(list(edgesCopy.keys())[0])
                q.put(aux)
                comp += 1
                component = []
            # Puxa o proximo da fila
            v = q.get()

            # marca elemento como visitado
            visited.append(v.val)
            component.append(v)
            
            # percorre lista de arestas de i
            for j in edgesCopy[v.val]:
                # coloca na fila se ja nao estiver ou se nao tiver sido visitado
                if j not in visited and j not in q.queue:
                    aux = Vertex(j, v.val, v.level+1)
                    q.put(aux)
            
            edgesCopy.pop(v.val) # remove vertice para ficar mais facil buscar por grafos desconexos
        
        # salva o ultimo componente
        f.write("\nComponente "+str(comp)+":\n")
        f.write("Tamanho: "+str(len(component))+"\n")
        component_size = len(component)
        if component_size == 1:
            n_single += 1
        if component_size < sml_comp:
            sml_comp = component_size
        if component_size > big_comp:
            big_comp = component_size
        while len(component) > 0:
            f.write(str(component.pop(0))+"\n")
        f.close()
        
        f = open("temporaryAndUselessButYetVeryUsefulFileThatNoOneShallKnowAboutItsExistence.txt", 'r')
        discardline, remaining = f.readline(), f.read()
        t = open(outputpath,"w")
        t.write("Total de Componentes: "+str(comp)+"\n")
        t.write("Maior componente: "+str(big_comp)+" Menor Componente: "+str(sml_comp)+"\n")
        t.write("Numero de componentes de tamanho 1: "+str(n_single))
        t.write(remaining)
        t.close()
        f.close()
        os.remove("temporaryAndUselessButYetVeryUsefulFileThatNoOneShallKnowAboutItsExistence.txt")

    def updatedist(self, val, totaldist, distances):
        for i in self.edges[val]:
            if self.weighted:
                dist = totaldist + self.edges[val][i]
            else:
                dist = totaldist + 1
            if self.distance[i].visited == False and dist < self.distance[i].distance:
                self.distance[i].distance = dist
                self.distance[i].parent = val
                heapq.heappush(distances, Ordering(i, dist, val))


    def dijkstra(self, start):
        '''
        Implementation of Dijkstra's algorithm.
        @param start: The starting/root vertex.
        '''
        if self.isDijkstraPossible == False:
            print("Is not possible to apply Dijkstra on this graph because it has a negative weighted edge.")
            return

        distances = []
        self.distance = ddict(Ordering)
        totaldistance = 0
        for i in self.edges:
            if i == start:
                v = Ordering(i, 0, 'R')
                self.distance[i] = v
                distances.append(v)
            else:
                self.distance[i] = Ordering(i, float('inf'), 'R')
        
        heapq.heapify(distances)
        while len(distances) > 0:
            v = heapq.heappop(distances)
            self.distance[v.val].visited = True
            totaldistance = v.distance
            self.updatedist(v.val, totaldistance, distances)

    def shortest_path(self, finish):
        path = []
        aux = finish
        while aux != 'R':
            path.append(aux)
            aux = self.distance[aux].parent
        path.reverse()
        
        return self.distance[finish].distance, path