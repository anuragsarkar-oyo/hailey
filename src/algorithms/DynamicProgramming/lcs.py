



def lcs(a, b):
  print(a,b)
  if len(a) < 1 or len(b) < 1:
    return 0 
  elif a[0] == b[0] : 
    return 1 + lcs(a[1:], b[1:])
  return max(lcs(a, b[1:]), lcs(a[1:], b))

def lcs_dp(a,b):
  if len(a) < 1 or len(b) < 1: 
    return 0 
  dp = [[0]*(len(b)+1)]*(len(a)+1)
  print(dp)
  for i in range(1,len(a)+1): 
    for j in range(1,len(b)+1): 
      if a[i-1] == b[j-1]: 
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  print(dp)
  return dp[len(a)][len(b)], dp
  
def print_lcs(dp, a, b):
  s = ""
  i = len(a)
  j = len(b)
  while i > 0 and j > 0: 
    if a[i-1] == b[j-1]: 
      s += a[i-1] 
      i -=1 
      j -= 1
    elif dp[i-1][j] > dp[i][j-1]: 
      i -= 1
    else: 
      j -= 1
  print(s[::-1])

a = "AGGTAB"
b = "GXTXAYB"

# print(lcs(a,b))

v, d = lcs_dp(a,b)
print_lcs(d, a, b)