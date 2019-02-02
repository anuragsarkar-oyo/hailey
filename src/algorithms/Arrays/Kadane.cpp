//
// Created by Anurag Sarkar on 2019-02-02.
//

#include <iostream>
#include <algorithm>

void Kadane(int arr[], int sizeOfArray) {
    int maxGlobal = arr[0];
    int maxSoFar = arr[0];
    for(int i=1; i<sizeOfArray; i++) {
        maxSoFar = std::max(arr[i],maxSoFar+arr[i]);
        maxGlobal = std::max(maxSoFar,maxGlobal);
    }
    std::cout << maxGlobal;
}


int main() {
    int arr[5] = {7,-2,-3,-4,-7};
    Kadane(arr,5);
    return 0;
}