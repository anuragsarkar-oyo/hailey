


def lis_dp(a): 
  dp = [0]*len(a)
  dp[0] = 1
  for i in range(1, len(a)):
    for j in range(i): 
      if a[i] > a[j] and dp[i] < dp[j] + 1: 
        dp[i] = 1 + dp[j]
      
  print(dp)
  return max(dp)


a = [4,3,1,4,2,5,6,7]
print(lis_dp(a))