class Solution:
	# @param A : tuple of integers
	# @return an integer
    def singleNumber(self, A):
        # not correct method
        # it should have constant space 
        hashMap = {}
        for val in A:
            if val not in hashMap:
                hashMap[val] = 1
            else:
                hashMap[val] += 1

            if hashMap[val] == 3:
                hashMap.pop(val)

        if len(hashMap) == 1:
            for key in hashMap:
                return key
        
        return -1


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
    print(sol.singleNumber(arr))