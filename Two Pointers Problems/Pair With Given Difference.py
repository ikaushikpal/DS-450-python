class Solution:
    # @param arr : list of integers
    # @param targetSum : integer
    # @return an integer
    def solve(self, arr, targetSum):
        hashMap = {}
        for i in range(len(arr)):
            if arr[i] not in hashMap:
                hashMap[arr[i]] = 1
            else:
                hashMap[arr[i]] += 1
        
        for key in hashMap.keys():
            a = key
            b = a - targetSum
            if b in hashMap:
                return 1
        return 0 


if __name__ == '__main__':
    arr = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322 ]
    x = 369
    s = Solution()
    print(s.solve(arr, x))