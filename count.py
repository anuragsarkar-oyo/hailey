def count(a, b, q) :
    curr = [0] * 10  # assuming max value to be 9
    dep = [0] * 10

    for v in b :
        curr[v] += 1
    print(curr)
    dep[0] = curr[0]
    for i in range(1, 10) :
        dep[i] = dep[i - 1] + curr[i]  # this is the only thing we care !!!
    print(dep)

    for query in q :
        print(dep[query])


count([1, 2, 3, 4, 5, 6, 7, 1, 1, 4], [0, 1, 4, 2, 1, 4, 3, 1, 0, 5], [3, 5])
