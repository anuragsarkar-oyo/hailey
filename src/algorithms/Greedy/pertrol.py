


def canCompleteCircuit(self, gas, cost):

        if not gas or not cost:
            return -1

        if sum(gas) < sum(cost): 
            return -1

        index = 0
        total = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                index = i+1
                total = 0
        return index
  
  
a = [1,2,3,4,5]
b = [2,2,2,2,2]

canCompleteCircuit(a,b)
