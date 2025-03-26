class Solution:
    def canPair(self, nums, k): 
        if len(nums) % 2: # if nums containing odd number of elements
            return False

        hashTable = {}

        for num in nums:
            rem = num % k

            if rem in hashTable:
                hashTable[rem] += 1
            else:
                hashTable[rem] = 1
        
        for x in hashTable:
            if x == 0:
                if hashTable[0]%2: #odd or not
                    return False

            elif 2 * x == k:
                if hashTable[x]%2: #odd or not
                    return False

            else:
                requiredReminder = k - x
                if requiredReminder not in hashTable:
                    return False
                        
                elif hashTable[requiredReminder] != hashTable[x]:
                    return False

        return True


if __name__ == '__main__':
    k = 2
    nums = [6, 14, 12, 14]

    print(Solution().canPair(nums, k))
    print(Solution().canPair([13, 13, 14, 1], 2))
    print(Solution().canPair([6, 14, 12, 14], 2))