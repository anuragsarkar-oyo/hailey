//
// Created by Anurag Sarkar on 2019-02-02.
//

#include <iostream>
#include <algorithm>

void subArrayFixedSum(int arr[], int sizeOfArray, int sum) {
    int start=0;
    int currentSum = arr[0];
    for(int i=1;i<sizeOfArray;i++) {


        while(currentSum > sum && start < i-1) {
            currentSum -= arr[start];
            start++;
        }
        if(currentSum == sum) std::cout << "found" << " " << start <<" " <<  i-1;
        currentSum += arr[i];
    }
}

int main() {
    int arr[5] = {1,2,3,4,5};
    int sum = 6;
    subArrayFixedSum(arr,5,sum);
}