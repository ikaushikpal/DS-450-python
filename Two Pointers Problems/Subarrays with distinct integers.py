class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def fact(self, num):
        res = 1
        for i in range(2, num+1):
            res *= i
        return res

    def solve(self, A, B):
        if len(A) == 0:
            return 0

        n = len(A)
        i = j = 0
        count = 0
        myDict = {}

        while i<n and j<n:
            if A[j] not in myDict:
                myDict[A[j]] = 1
                j += 1

            elif A[j] in myDict:
                myDict[A[j]] += 1
                j += 1
            
            if len(myDict) > B:
                temp = 1
                for key in myDict:
                    temp += myDict[key]

                while len(myDict)> B:
                    val = A[i]
                    myDict[val] -= 1

                    if myDict[val] == 0:
                        myDict.pop(val)
                    
                    i += 1
                count += temp

            # if len(myDict) == B:
            #     if j ==n and i == 0:
            #         count += n
            #     else:
            #         count += self.fact(j-i-1)
        if len(myDict) == B and i==0 and j==n:
            return n
        return count


if __name__ == '__main__':
    A =[ 5, 3, 5, 1, 3 ]
    B = 3
    print(Solution().solve(A, B))