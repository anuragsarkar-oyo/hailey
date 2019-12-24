

def uniq(a, b):
    a = list(a)
    b = list(b)
    for i in range(len(a)):
        if a[i] in b:
            a[i] = ""
    #print(a)
    return ''.join(a)

a = "hello world"
b = "hello"

print(uniq(a,b))
