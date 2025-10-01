#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

vector<vector<int>> vec;
int n, m;
vector<int> color;
int avoid = -1;
int num_color = 1;

void input(){
    // arquivo de texto
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        string s;
        vector<int> line;
        cin >> s;
        for(int j = 0; j < m; j++){
            char c = s[j];
            cout << c;
            if(c == '1')
                line.push_back(j/2);
        }
        cout << endl;
        vec.push_back(line);
        color.push_back(avoid);
    }
    return;
}

void bruteforce(int u){
    color[u] = 0;

    if(u >= n-1) return;
    int num = 0;
    for(int i = 0; i < vec[u].size(); i++){
        int v = vec[u][i]; // adjacente
        if(color[v] != avoid && color[u] == color[v]){//se a cor de um adjacente é igual, vai pra proxima cor e verifica denovo
            color[u]++;
            num++;
            i = 0;
        }
    }
    num_color = max(num, num_color);
    
    for(int i = 0; i < vec[u].size(); i++){
        int v = vec[u][i]; // adjacente
        if(color[v] == avoid)bruteforce(v);
    }
}

void export_as_dag(){
    ofstream file;
    string filename = "graph_example.txt";
    file.open(filename);
    cout << "exporting as " << filename << "..." << endl;
    for(int i = 0; i < vec.size(); i++){
        for(int j = 0; j < vec[i].size(); j++){
            file << i << " " << vec[i][j] <<"\n";
        }
    }
    file << "num of nodes: " << n << " num of colors " << num_color << endl;
    for(int i = 0; i < n; i++){
        file << color[i];
        file << endl;
    }
    file.close();
}

int main(){
    input();
    for(int i = 0; i < n; i++){
        if(color[i] == avoid)bruteforce(i);
    }
    
    export_as_dag();
}