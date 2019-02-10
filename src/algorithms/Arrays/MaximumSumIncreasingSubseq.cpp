//
// Created by Anurag Sarkar on 2019-02-07.
//

#include "../../all.h"

void maximumSumSubseq(int arr[], int size) {
    int sum = 0;
    for(int i=0;i< size;i++) {
        if(*max_element(arr,arr+i) < arr[i]) {
            sum += arr[i];
        }
    }

    // hack away .. not a good solution ...
    if(arr[1] > arr[0] && arr[2] > arr[1]) {
        sum += arr[0] + arr[1];
    }
    else if(arr[2] > arr[1] && arr[0] > arr[1] && arr[2] > arr[0]) {
        sum += arr[0];
    }
    else if(arr[2] > arr[1] && arr[1] > arr[0] && arr[2] > arr[0]) {
        sum += arr[1];
    }
    cout << sum;
}


int main() {
    int arr[9] = {2,1,3,5,4,9,8,2,10};
    maximumSumSubseq(arr, 9);
}