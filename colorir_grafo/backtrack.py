import csv

def main():
    grafo = ler_grafo("grafo25.csv")
    v = len(grafo)
    m = 8
    cores = [0] * v
   
    if (colorir_grafo(grafo, cores, 0, m)):
        print("Coloração do grafo encontrada: \n")
        for i in range(v):
            print(f"Vértice {i} -> Cor {cores[i]}\n")
    else:
        print(f"Não é possível colorir o grafo com {m} cores.\n")

def ler_grafo(arquivo):
    grafo = []
    with open(arquivo, newline='') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            grafo.append([int(x) for x in linha])
    return grafo

def pode_colorir(grafo, cores, vertice, cor):
    for i in range(len(grafo)):
        if grafo[vertice][i] == 1 and cores[i] == cor:
            return False
    return True

def colorir_grafo(grafo, cores, vertice, m):
    if vertice == len(grafo):
        return True
    cor = 1
    for cor in range(1, m+1):
        if(pode_colorir(grafo, cores, vertice, cor)):
            cores[vertice] = cor
            if(colorir_grafo(grafo, cores, vertice + 1, m)):
                return True
            cores[vertice] = 0; 

    return False

main()