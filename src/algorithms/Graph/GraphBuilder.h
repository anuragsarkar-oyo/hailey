//
// Created by Anurag Sarkar on 2019-02-10.
//

#ifndef HAILEY_GRAPHBUILDER_H
#define HAILEY_GRAPHBUILDER_H

#include "../../all.h"

class GraphBuilder {
public:
    void unDirectedNoWeight(vector<pair<int,int>> &vec, int size) {
        for(int i=0;i<size*2;i++) {
            vec.push_back(make_pair(i%size, (rand() % 10) + 1 ));
        }
    }

    void unDirectedWeight(vector<pair<int,int>> vec, int size) {

    }

    void directedNoWeight(vector<pair<int,int>> vec, int size) {

    }

    void DirectedWeight(vector<pair<int,int>> vec, int size) {

    }

};


#endif //HAILEY_GRAPHBUILDER_H
