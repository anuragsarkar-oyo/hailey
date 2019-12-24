import heapq

def mergeK(arrayOfArrays):
    heap = []
    print ('    ' + "val " + "k " + "i ")
    for i in range(len(arrayOfArrays)):
        heap.append((arrayOfArrays[i][0], i, 0))
    heapq.heapify(heap)
    result = []
    while heap:
        val, index_array, index_elem = heapq.heappop(heap)
        print ('pop: ', val, index_array, index_elem)
        result.append(val)
        if index_elem + 1 < len(arrayOfArrays[index_array]):
            heapq.heappush(heap, (arrayOfArrays[index_array][index_elem + 1],
                                  index_array, index_elem + 1))
    return result

arrayOfArrays = [
  [1, 5, 7, 11], 
  [2, 3, 4, 8, 9], 
  [3, 6, 9, 12, 15, 20]
  ]
print (mergeK(arrayOfArrays))
