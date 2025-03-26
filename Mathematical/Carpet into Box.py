# There is a carpet of a size a*b [length * breadth]. You are given a box of size c*d. The task is, one has to fit the carpet in the box in a minimum number of moves. 

# In one move, you can either decrease the length or the breadth of the carpet by half (floor value of its half).

# Note: One can even turn the carpet by 90 degrees any number of times, wont be counted as a move.

 
# Example 1:
# Input:
# A = 8, B = 13
# C = 6, D = 10
# Output:
# Minimum number of moves: 1
# Explanation:
# Fold the carpet by breadth, 13/2 i.e. 6, 
# so now carpet is 6*8 and can fit fine.
 

# Example 2:
# Input:
# A = 4, B = 8
# C = 3, D = 10
# Output:
# Minimum number of moves: 1
# Explanation: Fold the carpet by length , 4/2 i.e. 2,
# so now carpet is 2*8 and can fit fine.


class Solution:
    def carpetBox(self, A,B,C,D):
        # intuition 
        # always storing length as maximum and breadth as minimum
        boxLength, boxBreadth = max(C,D), min(C,D)
        carpetLength, carpetBreadth = max(A,B), min(A,B)
        moves = 0

        while carpetLength > boxLength or carpetBreadth > boxBreadth:
            if carpetLength > boxLength:
                carpetLength = carpetLength //2

            elif carpetBreadth > boxBreadth:
                carpetBreadth = carpetBreadth //2

            carpetLength, carpetBreadth = max(carpetLength, carpetBreadth), min(carpetLength, carpetBreadth)
            moves += 1
        return moves
# Time Complexity: O(log(max(A,B)))
# Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.carpetBox(8,13,6,10))
    print(sol.carpetBox(4,8,3,10))
