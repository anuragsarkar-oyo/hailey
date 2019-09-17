


def minpart_dp(arr): 
  total = sum(arr)
  dp = [[False]*(total+1)]*(len(arr)+1)
  print(dp)
  for i in range(len(arr)): 
    dp[i][0] = True
  for i in range(1,len(arr)+1): 
    for j in range(1,total+1): 
      dp[i][j] = dp[i-1][j]
      if arr[i-1] <= j: 
        dp[i][j] |= dp[i][j-arr[i-1]]
    print(dp)
    
  print(dp)
  
arr = [1, 2, 3]
minpart_dp(arr)
