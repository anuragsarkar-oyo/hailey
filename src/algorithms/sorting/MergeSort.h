//
// Created by Anurag Sarkar on 2019-02-02.
//

#ifndef HAILEY_MERGESORT_H
#define HAILEY_MERGESORT_H

#endif //HAILEY_MERGESORT_H

#include <vector>
//Mergesort is one of the earliest algorithms proposed for sorting. According to Donald Knuth,
////it was suggested by John von Neumann as early as 1945.


class MergeSort {
public:
    void mergeSort(int arr[], int start, int end) {
        if(start < end) {
            int median = (start + end) / 2;
            mergeSort(arr, start, median);
            mergeSort(arr, median + 1, end);
            merge(arr, start, end, median);
        }
    }

    void merge(int arr[], int start, int end, int median) {
        int i,j,k;
        int n1 = median - start + 1;
        int n2 =  end - median;
        int leftArray[n1];
        int rightArray[n2];

        for (i = 0; i < n1; i++)
            leftArray[i] = arr[start + i];
        for (j = 0; j < n2; j++)
            rightArray[j] = arr[median + 1+ j];
        i = 0; // Initial index of first subarray
        j = 0; // Initial index of second subarray
        k = start; // Initial index of merged subarray
        while (i < n1 && j < n2)
        {
            if (leftArray[i] <= rightArray[j])
            {
                arr[k] = leftArray[i];
                i++;
            }
            else
            {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        /* Copy the remaining elements of leftArray[], if there
           are any */
        while (i < n1)
        {
            arr[k] = leftArray[i];
            i++;
            k++;
        }

        /* Copy the remaining elements of R[], if there
           are any */
        while (j < n2)
        {
            arr[k] = rightArray[j];
            j++;
            k++;
        }
    }

};