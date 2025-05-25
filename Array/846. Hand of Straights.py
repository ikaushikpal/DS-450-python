# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

# Example 2:
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

# Constraints:
# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length


from typing import Counter, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        for card in sorted(c.keys()):
            card_size = c[card]
            if c[card] > 0:
                for i in range(card, card + groupSize):
                    c[i] -= card_size
                    if c[i] < 0:
                        return False
        return True
# Time Complexity: O(MlogM + MK)
# Space Complexity: O(M)
# where M is number of unique numbers in hand, N is the length of the hand and K is the groupSize


if __name__ == '__main__':
    sol = Solution()
    print(sol.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
    print(sol.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))
    print(sol.isNStraightHand([1,2,3,4,5,6], 2))