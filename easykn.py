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
easykn(foodPrice, weight)
