


def kClosestNumber(arr, k, x):
  arr = sorted(arr)
  p, q = 0, k
  for _ in range(len(arr)-k):
    if abs(x-arr[p]) > abs(x - arr[q]) and arr[p] <= arr[q]:
      p += 1
      q += 1
  return arr[p:q]


arr = [12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56]
print(sorted(arr))
k = 4
x = 35
print(kClosestNumber(arr,k,x ))