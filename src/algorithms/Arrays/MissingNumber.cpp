//
// Created by Anurag Sarkar on 2019-02-02.
//

#include <iostream>
#include <algorithm>
#include <vector>

void missingNumberInArray(int arr[], int sizeOfArray) {
    int maxValue = *std::max_element(arr,arr+sizeOfArray);
    int lookup[maxValue];
    memset(lookup, 0, maxValue);
    for(int i=0; i<sizeOfArray; i++) {
        lookup[arr[i]-1]++;
    }
    std::vector<int>v;
    for(int i=0;i<maxValue;i++) {
        if(lookup[i] == 0 ) v.push_back(i+1);
    }
    for(auto i : v) std::cout << i << " ";
}

int main() {
    int arr[5] = {1,2,3,4,8};
    missingNumberInArray(arr,5);
}