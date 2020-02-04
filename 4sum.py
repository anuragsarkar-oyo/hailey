def fourSum(arr, n, k) :
    sumDict = dict()
    uniqCombinations = []
    for i in range(0, n - 1) :
        for j in range(i + 1, n) :
            try :
                sumDict[arr[i] + arr[j]].append((i, j))
            except :
                sumDict[arr[i] + arr[j]] = [(i, j)]

    for key in sumDict :
        try :
            a, b = sumDict[k - key], sumDict[key]
            for avalue in a :
                for bvalue in b :
                    if avalue[0] not in bvalue and avalue[1] not in bvalue :
                        uniq = sorted([arr[avalue[0]], arr[avalue[1]], arr[bvalue[0]], arr[bvalue[1]]])
                        # print(uniq)
                        uniqCombinations.append(uniq)
                    else :
                        continue
        except :
            continue

    return set(tuple(i) for i in uniqCombinations)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
k = 9
print(fourSum(arr, len(arr), k))
