//
// Created by Anurag Sarkar on 2019-02-06.
//

#include <iostream>
#include <algorithm>

// find the subarray with a given sum = 0
void subarrayZero(int arr[], int size) {
    int start=0;
    int currentSum = arr[0];
    for(int i=1;i<size;i++) {


        while(currentSum > 0 && start < i-1) {
            currentSum -= arr[start];
            start++;
        }
        if(currentSum == 0) std::cout << "found" << " " << start <<" " <<  i-1;
        currentSum += arr[i];
    }
}


int main() {
    int arr[5] = {-1,-2,0,3,1};
    subarrayZero(arr, 5);
}