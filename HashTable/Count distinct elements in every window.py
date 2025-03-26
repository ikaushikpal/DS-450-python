class Solution:
    def countDistinct(self, arr:list, n:int, k:int)->list:
        output = []
        if n < k:
            return output

        windowSet = {}
        for i in range(k):
            val = arr[i]
            # adding new element in window
            if val not in windowSet:
                windowSet[val] = 1
            else:
                windowSet[val] += 1

        for i in range(k, n):
            val = arr[i]

            output.append(len(windowSet))

            # remove boundary element
            windowSet[arr[i-k]] -= 1
            if windowSet[arr[i-k]] == 0:
                del windowSet[arr[i-k]]

            # adding new element in window
            if val not in windowSet:
                windowSet[val] = 1
            else:
                windowSet[val] += 1

        output.append(len(windowSet))
        return output
    

if __name__ == '__main__':
    print(Solution().countDistinct([1,2,1,3,4,2,3], 7, 4))