#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

vector<string> v;
int n, m;
char target = '.';//Estou usando ponto como branco, se quiser pode trocar aqui! e a parede pode ser qq caracter
vector<string>dag;

void input(){
    // arquivo de texto
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        if(s.size() < m) s+=('.');//necessario para arrumar input
        v.push_back(s);
    }
    return;
}

char bruteforce(int x, int y){//previus dir
    if(x == n-1 && y == m-1){
        cout << x <<  " " << y << endl;
        v[x][y]='X';
        return '!';
    }
    v[x][y] = 'x';
    pair<int,int> dir[4] = {{1,0},{0,1}, {-1,0}, {0,-1}};//dir baixo esq cima
    for(int i = 0; i < 4; i++){
        int xx = x + dir[i].first;
        int yy = y + dir[i].second;
        
        if(xx < 0 || yy < 0 || xx >= n || yy >= m)continue;//evitar bordas
        
        if(v[xx][yy] == target){
            dag.push_back(to_string(x) + "," + to_string(y) + " " + to_string(xx) + "," + to_string(yy));
            char c = bruteforce(xx,yy);
            if(c == '!') {
                v[x][y] = c;
                return c;
            }
        }
    }
    v[x][y]='.';
    return 'x';
}

void export_as_dag(){
    ofstream file;
    file.open("example.txt");
    cout << "exporting..." << endl;
    for(int i = 0; i < dag.size(); i++){
        file << dag[i] <<"\n";
    }
    file.close();
}

int main(){
    input();
    bruteforce(0,0);
    export_as_dag();

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << v[i][j];
        }
        cout << endl;
    }
}