//
// Created by Anurag Sarkar on 2019-02-02.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>


void equilibriumPoint(int arr[], int sizeOfArray) {
    int i = 0;
    int sum = 0;
    int totalSum = std::accumulate(arr,arr+sizeOfArray,0);
    while(i < sizeOfArray+1) {
        sum += arr[i];
        if(sum*2 == totalSum-arr[i+1]) {
            std::cout << "yep";
            break;
        }
        i++;
    }
}

int main() {

    int arr[7] = {1,2,3,4,3,2,1};
    equilibriumPoint(arr,7);
}