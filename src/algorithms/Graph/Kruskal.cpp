//
// Created by Anurag Sarkar on 2019-02-10.
//

#include "GraphBuilder.h"

void kruskal(vector<pair<int,int>> graph) {
    // step 1 is to sort the graph in desc order
    sort(graph.begin(), graph.end());

}

int main() {
    vector< pair<int,int> > connections;
    GraphBuilder().unDirectedNoWeight(connections, 10);
    for(auto i : connections) cout << i.first << " " << i.second << '\n';
//    Kruskal(connections);
}