

def sort(arr, ty): 
  # print(arr, ty)
  if len(arr) < 2: 
    return arr
  left = len(arr)//2
  return merge(sort(arr[:left], "left"), sort(arr[left:], "right"))

def merge(a, b):
  print("before merge", a, b)
  x = []
  i,j = 0,0
  while i < len(a) and j < len(b): 
     if a[i] <= b[j]: 
       x.append(a[i])
       i += 1
     elif a[i] > b[j]: 
       x.append(b[j])
       j += 1
  while i < len(a): 
    x.append(a[i])
    i += 1
  while j < len(b): 
    x.append(b[j])
    j += 1
  print("merge: " , x)
  return x


arr = [1,3,2,4,7,4,0,7,4,3]
print(sort(arr, "mid"))
print(sorted(arr))