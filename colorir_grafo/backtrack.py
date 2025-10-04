import csv

def main():
    grafo = ler_grafo("grafo25.csv")
    v = len(grafo)
    m = 8
    cores = [0] * v
   
    if colorir_grafo(grafo, cores, 0, m):
        print("Coloração do grafo encontrada.\n")
        for i in range(v):
            print(f"Vértice {i} -> Cor {cores[i]}")
        
        exportar_grafo_txt(grafo, cores, "resultado_backtrack.txt", m)
        print("\nGrafo exportado para 'resultado_backtrack.txt'")
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
    for cor in range(1, m+1):
        if pode_colorir(grafo, cores, vertice, cor):
            cores[vertice] = cor
            if colorir_grafo(grafo, cores, vertice + 1, m):
                return True
            cores[vertice] = 0
    return False

def exportar_grafo_txt(grafo, cores, nome_arquivo, m):
    with open(nome_arquivo, "w") as f:
        v = len(grafo)
        # Exporta arestas
        for i in range(v):
            for j in range(i+1, v):  # evitar duplicar arestas
                if grafo[i][j] == 1:
                    f.write(f"{i} {j}\n")
        # Informações do grafo
        f.write(f"num of nodes: {v} num of colors {max(cores)}\n")
        # Exporta cores dos nós
        for cor in cores:
            f.write(f"{cor}\n")

main()
