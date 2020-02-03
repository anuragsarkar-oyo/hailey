

from collections import OrderedDict as orderDict
a = [1 ,1 , 1, 1, 1]

def pairs(arr):
    c = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] != arr[j]:
                c += 1

    return c
#print pairs(a)


def seg(arr):
    x = orderDict()
    for val in arr:
        try:
            x[val] += 1
        except:
            x[val] = 1

    return len(x.keys()), x.values()

_, vals = seg(a)

def count(vals, k):
    index = 0
    while k >= 0:
        print vals
        for i in range(len(vals)):
            if vals[i] > vals[index]:
                index = i
        vals[index] -= 1
        vals.append(1)
        k -= 1


    sumTotal = 0
    for i in range(len(vals)):
        for j in range(i, len(vals)):
            sumTotal += vals[i]*vals[j]

    print sumTotal
    return sumTotal


answer = count(vals, 4)
