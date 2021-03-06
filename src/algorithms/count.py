

def countFreq(arr, n):

    # Subtract 1 from every element so that
    # the elements become in range from 0 to n-1
    for j in range(n):
        arr[j] = arr[j] - 1

    # Use every element arr[i] as index
    # and add 'n' to element present at
    # arr[i]%n to keep track of count of
    # occurrences of arr[i]
    for i in range(n):
        arr[arr[i] % n] = arr[arr[i] % n] + n

    # To print counts, simply print the
    # number of times n was added at index
    # corresponding to every element
    for i in range(n):
        print(i + 1, "->", arr[i] // n)

arr = [1,2,3,1,2,1,3,1]
freq = countFreq(arr, len(arr))

