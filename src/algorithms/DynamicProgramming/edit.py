




def edit_dp(a, b): 
  
  dp = [[0]*(len(a)+1)]*(len(b)+1)
  
  for i in range(1,len(a)):
    for j in range(1,len(b)): 
      if a[i-1] == b[i-1]: 
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(min(dp[i-1][j], dp[i][j-1]),dp[i-1][j-1])
      
  print(dp)
  
a = "anurag"
b = "abhirup"

edit_dp(a,b)