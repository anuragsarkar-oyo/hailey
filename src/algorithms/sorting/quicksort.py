

def sort(arr, low, high): 
  
  if low <high: 
    p = partition(arr, low, high) 
    sort(arr, low, p-1) 
    sort(arr, p+1, high)
  return arr

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

arr = [1,3,2,4,7,4,0,7,4,3]
print(sort(arr, 0, 9))
print(sorted(arr))