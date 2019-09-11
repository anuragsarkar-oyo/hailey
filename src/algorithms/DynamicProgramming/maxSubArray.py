


def maxSubArray(arr):
  max_yet = arr[0]
  max_now = arr[0]
  for i in range(1,len(arr)):
    print(max_yet, max_now, arr[i])
    max_now = max(arr[i], max_now+arr[i])
    max_yet = max(max_yet, max_now)
    
  print(max_yet)
  
arr = [-1,2,4,-3,-5,6,-1]
maxSubArray(arr)
