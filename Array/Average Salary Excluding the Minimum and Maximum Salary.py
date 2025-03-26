# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 
# Example 1:
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500


# Example 2:
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
 

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        maximum = minimum = salary[0]
        total = 0

        for val in salary:
            total += val
            
            if val > maximum:
                maximum = val
            elif val < minimum:
                minimum = val
        
        return (total - maximum - minimum) / (len(salary) - 2)
# Time Complexity : O(N)
# Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.average([4000,3000,1000,2000]))
    print(sol.average([1000,2000,3000]))
