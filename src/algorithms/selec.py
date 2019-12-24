

# n trains entry time and there is exit time

# find the max number of platforms ... greedy


arr = [1 , 2, 3 , 4]
dep = [3, 3, 4 , 5]

def minPlatform(arrival, dept):

    count = 1 # initially we have 0 train 1 platform
    # this is base case
    # sort this array (not really but do it )
    i = 1 # arrival
    j = 0 # departure
    result = 1
    while i < len(arrival) and j < len(dept):

        if arrival[i] < dept[j]: # new train comes
            count += 1
            i += 1 # increse arrival time
            if(count > result):
                result = count
        else:
            count -= 1
            j += 1 # increse departure
        #i += 1
        #j += 1

    print(result)

def hackySol(arr, dep): # not recommended

    # arr = [ 1 - arr, 2 - arr, 3 -arr ,4 -arr ]
    # dep = [3 -dep, 3 -dep, 4 -dep, 5 -dep]
    # sort(arr + dep) => [1a, 2a, 3a, 3d, 3d, 4a, 4d, 5d]
    # logic ?


minPlatform(arr, dep)
