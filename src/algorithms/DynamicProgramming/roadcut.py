


def roadcut_dp(arr): 
  max_val = -2**32
  dp = [0]*(len(arr)+1)
  for i in range(1,len(arr)+1): 
    for j in range(i): 
      max_val = max(arr[j] + dp[i-j-1], max_val)
      dp[i] = max_val 
      print(dp)
      
  print(dp)
  
  
arr = [1, 5, 8, 9, 10, 17, 17, 20]
roadcut_dp(arr)