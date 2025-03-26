# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 
# Example 1:
# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.


# Example 2:
# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.


# Example 3:
# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# Explanation: It is best to choose the first 3 players. 


from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # LIS variant
        N = len(scores)
        players = [(age, score) for age, score in zip(ages, scores)]
        players.sort()

        ans = 0
        dp = [0] * N

        for i in range(N-1, -1, -1):
            score = players[i][1]
            dp[i] = score
            
            for j in range(i+1, N):
                if players[i][1] <= players[j][1]:
                    dp[i] = max(dp[i], dp[j]+score)
            ans = max(ans, dp[i])
        return ans
# Time Complexity: O(N^2)
# Space Complexity: O(N)


if __name__ == "__main__":
    sol = Solution()
    print(sol.bestTeamScore([1,3,5,10,15], [1,2,3,4,5]))
    print(sol.bestTeamScore([4,5,6,5], [2,1,2,1]))
    print(sol.bestTeamScore([1,2,3,5], [8,9,10,1]))