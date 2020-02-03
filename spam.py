

n = int(input())
while n > 0:
    p = int(input())
    m = {}
    for _ in range(p):
        t = [x for x in input().split(" ")]
        if int(t[1]) == 1:
            try: # 1
                m[t[0]][0] += 1
            except:
                m[t[0]] =  [1, 0]
        else: # 0
            try:
                m[t[0]][1] += 1
            except:
                m[t[0]] =  [0, 1]
    s = 0
    for k, v in m.items():
        if v[0] > v[1]:
            s += v[0]
        else:
            s += v[1]
        print(k, v)
    
    n -= 1
    print(s)

