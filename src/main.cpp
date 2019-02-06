#include <iostream>
#include <algorithm>
#include "algorithms/sorting/QuickSort.h"

int main() {
    std::cout << "Hello, World! to my programming practice ..." << std::endl;
    std::cout << "CAUTION this is not meant for competitive coding or to crack any interview ... " << std::endl;
    std::cout << "this is to keep ME busy when my friends are out drinking ......" << std::endl;
    int arr[5] = {1,4,2,3,5};
    QuickSort().quickSort(arr,0,4);
    QuickSort().print(arr, 5);
    return 0;
}