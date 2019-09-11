


def coinChange(arr, value):
  
  dp = [[0]*(value+1)]*len(arr)
  
  for i in range(len(arr)):
    dp[i][0] = 1
  
  # print(dp)
  
  for i in range(len(arr)):
    for j in range(1,value+1):
      x = dp[i][j-arr[i]] if j-arr[i] >=0 else 0  # exclude the jth term
      y = dp[i-1][j] if i >=1 else 0 # use the last element 
      dp[i][j] = (x + y)
  # print(dp)
  print(dp[len(arr)-1][value])


arr = [5, 7, 11] 
m = len(arr) 
n = 12
coinChange(arr, n)
