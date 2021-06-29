class Solution:
	# @param A : list of integers
	# @return a list of list of integers

    def twosum(self, arr, index, target):
        i = index
        j = len(arr) - 1

        while i<j:
            if arr[i] + arr[j] == target:
                temp = [arr[index-1], arr[i], arr[j]]

                if len(self.res)>0:
                    if self.res[0] != temp:
                        self.res.insert(0, temp)
                else:
                    self.res.insert(0, temp)

                i += 1
                j -= 1
            
            elif arr[i] + arr[j] < target:
                i += 1
            else:
                j -= 1

    def threeSum(self, arr):
        self.res = []
        arr.sort()

        for i in range(len(arr)-2):
            if (i==0) or (i and arr[i] != arr[i-1]):
                self.twosum(arr, i+1, -arr[i])
     
        return self.res


if __name__ == '__main__':
    arr = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.threeSum(arr))