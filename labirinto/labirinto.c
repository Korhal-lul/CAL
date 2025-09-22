#include <stdio.h>
#include <stdlib.h>


#define N 61




int isSafe(int maze[N][N], int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < N && maze[x][y] == 0);
}

int solveMazeUtil(int maze[N][N], int x, int y) {

    return 0;
}

void printMaze(int maze[N][N]){
    printf("Caminho no labirinto:\n");
    printf("%c ",219);
    for (int j = 1; j < N+1; j++) {
        printf("%c",219);
    }
    printf("\n");
    for (int i = 0; i < N; i++) {
        printf("%c",219);
        for (int j = 0; j < N; j++) {
            if(maze[i][j] == 1){
                printf("%c",219);
            }else if(maze[i][j] == 2){
                printf("%c", 248);
            }else{
                printf(" ");
            }
            //printf("%d ", maze[i][j]);
        }
        printf("%c\n",219);
    }
    for (int j = 0; j < N; j++) {
        printf("%c",219);
    }
    printf(" %c\n",219);
}

int solveMaze(int maze[N][N]) {
    // Iniciar a busca a partir do ponto de partida (0, 0)
    /*
    if (solveMazeUtil(maze, 0, 0) == 0) {
        printf("Não há solução para o labirinto.\n");
        return 0;
    }
    */

    // Imprimir
    printMaze(maze);
    return 1;
}

void loadMaze(int maze[N][N], char *fname){
    //gere um nesse site, cole no arquivo lab.txt ou outro
    //https://www.dcode.fr/maze-generator
    //veja quantas linhas e colunas tem e altere o valor de N
    //uma diferença de 1 na quantia de colunas geralmente não causa problema
    //pois o algoritmo aqui inclui uma borda extra
    FILE *f;
    int i, lineN = 0;
    char line[N+10];
    f = fopen(fname, "r");
    while(fgets(line, sizeof(line), f) != NULL){
        i = 0;
        if(line[0]=='0' || line[0] == '1'){
            while(line[i] != '\0'){
                maze[lineN][i] = line[i] - '0';
                i++;
                if(i>=N) break;
            }
            lineN++;
            if(lineN>=N){ break;}
        }
    }

    printf("i: %d, LineN: %d\n", i, lineN);

}

int main() {
    /*
    //1 = parede
    //0 = vazio
    //2 = caminho
    int maze[N][N] = {
        {0, 1, 0, 0, 0, 0, 0, 1, 0, 0},
        {0, 1, 0, 1, 1, 0, 1, 1, 0, 1},
        {0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        {1, 1, 0, 1, 0, 1, 1, 1, 1, 0},
        {0, 0, 0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0, 1, 1, 0, 1, 1},
        {0, 1, 1, 1, 1, 1, 1, 0, 1, 0},
        {0, 1, 0, 0, 0, 1, 0, 0, 0, 0},
        {0, 1, 0, 1, 0, 1, 1, 1, 1, 0},
        {0, 0, 0, 1, 0, 0, 0, 0, 0, 0}
    };
    */
    int maze[N][N];

    loadMaze(maze, "lab.txt");

    if (solveMaze(maze)) {
        printf("Labirinto resolvido!\n");
    } else {
        printf("Não foi possível encontrar uma solução.\n");
    }

    return 0;
}

