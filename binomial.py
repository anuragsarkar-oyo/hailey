def binomialCount(n, r) :
    if n == 0 or r == 0 :
        return 1
    return binomialCount(n - 1, r - 1) + binomialCount(n - 1, r)  # this is bad


# formulae : =====  ncr = n-1cr-1 + n-1cr
# ith index that is n
# jth index that is r
def goodBinomialCount(n, r) :
    # dp :)
    dp = [[0] * (r + 1)] * (n + 1)
    for i in range(n + 1) :
        for j in range(r + 1) :
            if i == 0 or j == i :
                dp[i][j] = 1
            else :
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp  # iska last value is nothing but ncr  ?? so this combination
    # to calculate permutation we just multiply it with r!


def rFact(r) :
    if r == 1 :
        return 1
    return r * rFact(r - 1)


def goodrFact(r) :
    dp = [0] * (r + 1)
    dp[0] = 1
    for i in range(1, r + 1) :
        if i == 1 :
            dp[i] = 1
        else :
            dp[i] = dp[i - 1] * i
    print(dp)
    return dp[r]


def decreasing(n) :
    dp = [[0] * 10] * (n + 1)  # got this ?
    # base condt... says that 0 size of n will hve only one solution
    for i in range(10) :
        dp[0][i] = 1  # why is this not 0 ? this means it is an empty sols.

    # base condt -> value 9
    for i in range(1, n + 1) :
        dp[i][9] = 1  # this will handle 9 , 99 , 999

    # core logic !!!!
    for i in range(1, n + 1) :  # this goes from 1 to n(inclusive)
        for j in range(8, -1, -1) :  # this goes to 8 to 0 (inclusive) # 8 will always be a solution
            dp[i][j] = dp[i - 1][j] + dp[i][j + 1]  # add all possible values and add the prev result


# what does this dp signify ?
# i -> nth bit kya hai
# j -> usse bade number chiye  ?
# i = 2, j = 4
# dp[2][4] = dp[1][4] + dp[2][5]

    return dp

print(decreasing(2))