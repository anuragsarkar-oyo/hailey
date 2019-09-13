


def maxSubArray(arr):
  max_yet = arr[0]
  max_now = arr[0]
  for i in range(1,len(arr)):
    print(max_yet, max_now, arr[i])
    max_now = max(arr[i], max_now+arr[i])
    max_yet = max(max_yet, max_now)
    
  print(max_yet)
  
def maxSubArrayWithIndex(arr):
  start = 0
  end = 0
  s = 0 # always have a independent mover in these questions 
  max_yet = arr[0]
  max_total = arr[0]
  for i in range(1, len(arr)): 
    max_yet = max_yet + arr[i]
    if max_yet < 0:
      s = i + 1
      max_yet = 0
    if max_yet > max_total:
      max_total = max_yet
      end = i
      start = s
  print(start+1, end)
  print(max_total)
    
  
arr = [-1,2,4,-3,-5,2,-1]
# maxSubArray(arr)
maxSubArrayWithIndex(arr)
