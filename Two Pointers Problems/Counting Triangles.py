class Solution:
	# @param A : list of integers
	# @return an integer
    def nTriang(self, A):
        n = len(A)
        res = set()
        count = 0
        A.sort()

        for i in range(n - 1, 0, -1):
            l = 0;
            r = i - 1;
            while(l < r):
                if(A[l] + A[r] > A[i]):
                    count += r - l;
                    r -= 1;
                
                else:
                    l += 1;

        return count

arr = [10, 21, 22, 100, 101, 200, 300]
print(Solution().nTriang(arr))

