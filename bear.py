
import math 
n = int(input())
# print(n)
while n > 0:
    t = int(input())
    # print(t)
    check = 5 # 25 125  and so on ...
    nx = 0 # ending zeros 
    while check < t:
      nx += math.floor(t/check)
      check *= 5
        
    print(check ,nx)
    n -= 1