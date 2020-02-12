def hardkn(foodPrice, weight) :  # suboptimal solution
    # foodPrice = [(1,5),(2,1),(4,4),(6,2),(7,1)]
    # weight = 10
    # y = f(x , z) -> 2d dp right ?
    # we dont care about sorting
    dp = [[0] * weight] * len(foodPrice)
    print(dp)
    # f(x, z) = f(x-1, z-w) + f(x-1, z) ( yes and no)
    # dynamic programming would always include worst case solutions !!!!
    for i in range(len(foodPrice)) :
        for j in range(weight + 1) :
            if i == 0 or j == 0 :  # dont have food or dont have space in bag
                dp[i][j] = 0
            elif foodPrice[i][0] < j :  # minimize the total money spent
                dp[i][j] = max(foodPrice[i][1] + dp[i - 1][j - foodPrice[i][0]], dp[i - 1][j])
            else :
                dp[i][j] = dp[i - 1][j]
    return dp
    #
    # foodPrice[i][1] + dp[i - 1][j - foodPrice[i][0]] -> optimal solution so you will not choose dp[i - 1][j]
    # foodPrice[i][1] +ve number, dp[i - 1][j - foodPrice[i][0]] +ve =>


def easykn(foodPrice, weight) :
    # foodPrice = [(1,5),(2,1),(4,4),(6,2),(7,1)]
    # weight = 10
    totalPrice = 0
    price = sorted(foodPrice, key = lambda x : x[1])
    currentWeight = 0
    print(price)
    mat = []
    i = 0
    while currentWeight < weight :
        if currentWeight + price[i][0] < weight :
            currentWeight += price[i][0]
            totalPrice += price[i][1]
            i += 1
            mat.append([currentWeight, totalPrice])
        else :
            residue = weight - currentWeight
            priceOfResidue = residue * (price[i][1] / price[i][0])  # what i want * what is price of each unit
            currentWeight += residue
            totalPrice += priceOfResidue
            i += 1
            mat.append([currentWeight, totalPrice])

    print(totalPrice)
    print(mat)


foodPrice = [(1, 5), (2, 1), (4, 4), (6, 2), (7, 1)]
weight = 10
hardkn(foodPrice, weight)
