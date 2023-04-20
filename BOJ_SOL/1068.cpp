#include <iostream>
#include <vector>

using namespace std;

int n, del_node;
vector<int> nodes, graph[50];

void delete_node(int node) {
    for(int i = 0; i < graph[node].size(); i++){
        int child = graph[node][i];
        delete_node(child);
    }
    graph[node].clear();
    for (int i = 0; i < n; i++){
        for (int j = 0; j < graph[i].size(); j++){
            if(graph[i][j] == node){
                graph[i].erase(graph[i].begin() + j);
                break;
            }
        }
    }
}

int find_root(const vector<int> &nodes){
    for (int i = 0; i < nodes.size(); i++){
        if(nodes[i] == -1){
            return i;
        }
    }
    return -1;
}

int count_leaf(const vector<int> graph[], int v){
    if(graph[v].empty()){
        return 1;
    }
    int cnt = 0;
    for(int i = 0; i < graph[v].size(); i++){
        cnt += count_leaf(graph, graph[v][i]);
    }
    return cnt;
}

int main(){
    cin >> n;
    nodes.resize(n);
    for (int i = 0; i < n; i++){
        cin >> nodes[i];
        if(nodes[i] != -1){
            graph[nodes[i]].push_back(i);
        }
    }
    cin >> del_node;
    delete_node(del_node);
    int root = find_root(nodes);
    if(del_node == root){
        cout << 0 << endl;
    }
    else{
        cout << count_leaf(graph, root) << endl;
    }
    return 0;
}