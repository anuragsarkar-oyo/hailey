


class Solution:
    def advantageCount(self, A, B):
        A.sort()

        left = 0
        right = len(A) - 1

        for value, index in sorted([(value, index) for index, value in enumerate(B)], reverse=True):
            if value >= A[right]:
                num = A[left]
                left += 1
            else:
                num = A[right]
                right -= 1

            B[index] = num

        return B
  
# A = [2,7,11,15]
# B = [1,10,4,11]
A = [12,24,8,32]
B = [13,25,32,11]

print(Solution().advantageCount(A,B))