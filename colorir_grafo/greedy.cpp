#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<vector<int>> vec;   // lista de adj
vector<int> color;
int n;                     // num de nos
int num_colors = 0;        // num de cores

void input(const string &filename){
    ifstream file(filename);
    string line;
    int row = 0;

    while(getline(file, line)){
        vector<int> adj;
        stringstream ss(line);
        string value;
        int col = 0;

        while(getline(ss, value, ',')){
            int val = stoi(value);
            if(val == 1){
                adj.push_back(col);
            }
            col++;
        }

        vec.push_back(adj);
        row++;
    }

    n = row;
    color.assign(n, -1);
    file.close();
}

void greedy_coloring(){
    color[0] = 0; 
    num_colors = 1;

    for(int u = 1; u < n; u++){
        vector<bool> available(n, true);

        // marca as cores usadas pelos vizinhos
        for(int v : vec[u]){
            if(color[v] != -1)
                available[color[v]] = false;
        }

        // escolhe a primeira cor disponível
        int cr;
        for(cr = 0; cr < n; cr++){
            if(available[cr])
                break;
        }

        color[u] = cr;
        if(cr + 1 > num_colors)
            num_colors = cr + 1;
    }
}

void export_as_txt(const string &filename){
    ofstream file(filename);

    cout << "num of nodes: " << n << " num of colors " << num_colors << endl;
    cout << "exporting as " << filename << "..." << endl;

    for(int i = 0; i < vec.size(); i++){
        for(int j : vec[i]){
            if(i < j) // evita duplicar arestas
                file << i << " " << j << "\n";
        }
    }

    file << "num of nodes: " << n << " num of colors " << num_colors << endl;

    for(int i = 0; i < n; i++){
        file << color[i] << endl;
    }

    file.close();
}

int main(){
    string input_file = "grafo25.csv";
    string output_file = "resultado_greedy.txt";

    input(input_file);
    int min_colors = 1e9;
    for(int i = 0; i < n; i++){
        greedy_coloring();
        min_colors = min(min_colors, num_colors);
    }
    num_colors = min_colors;
    export_as_txt(output_file);

    return 0;
}
