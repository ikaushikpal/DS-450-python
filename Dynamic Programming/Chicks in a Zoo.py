# Initially, the zoo have a single chick. A chick gives birth to 2 chicks every day and the life expectancy of a chick is 6 days. Zoo officials want to buy food for chicks so they want to know the number of chicks on an Nth day. Help the officials with this task.
 

# Example 1:
# Input: N = 2 
# Output: 3
# Explanation: First day there is only 1 chick.
# On second day total number of chicks = 3. 


# Example 2:
# Input: N = 3
# Output: 9
# Explanation: First day there is only 1 chick.
# On second day total number of chicks = 3.
# On third day total number of chicks = 9


class Solution:
	def NoOfChicks(self, N):
		dp = [0] * N
		dp[0] = 1
		chick = 1
		for i in range(1, N):
		    if i >= 6:
		        chick -= dp[i - 6]
		    dp[i] = chick << 1
		    chick += dp[i]
		return chick


if __name__ == '__main__':
    sol = Solution()
    print(sol.NoOfChicks(8))
        
