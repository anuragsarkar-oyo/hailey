

def numberOfPaths(m, n): 
# If either given row number is first 
# or given column number is first 
    if(m == 1 or n == 1): 
        return 1
  
# If diagonal movements are allowed 
# then the last addition 
# is required. 
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)
  
  
x = [[0] * 2]* 2
print(numberOfPaths( 5, 10))