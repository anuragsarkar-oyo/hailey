//
// Created by Anurag Sarkar on 2019-02-02.
//

#ifndef HAILEY_QUICKSORT_H
#define HAILEY_QUICKSORT_H

#endif //HAILEY_QUICKSORT_H

class QuickSort {
public:
    void quickSort(int arr[], int begin, int end) {
        if(begin < end) {
            int p = partition(arr, begin, end);
            quickSort(arr, begin, p-1);
            quickSort(arr, p+1, end);
        }
    }

    int partition(int arr[], int begin, int end) {
        int pivot = arr[end];
        int i = begin;
        for(int j=begin; j<end; j++) {
            if(arr[j] < pivot) {
                std::swap(arr[i],arr[j]);
                i += 1;
            }
        }
        std::swap(arr[i],arr[end]);
        return i;
    }

    void print(int arr[], int size) {
        for(int i=0; i< size; i++) {
            std::cout << arr[i] << " ";
        }
    }
};