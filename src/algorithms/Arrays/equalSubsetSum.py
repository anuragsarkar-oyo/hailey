
# wrong solution have to solve it with dp 

def equalSubsetSum(arr):
  arr = sorted(arr)
  right = sum(arr)
  left = 0
  i = 0
  while i < len(arr):
    print(left, right)
    if left == right:
      return True
    left += arr[i]
    right -= arr[i]
    i += 1
  return False

arr = [1,2,3,4,5,6,7]
print(equalSubsetSum(arr))