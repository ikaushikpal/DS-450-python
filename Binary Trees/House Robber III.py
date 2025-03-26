# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def cleverThief(self, house):
        if house is None:
            return 0, 0
        
        left_house = self.cleverThief(house.left)
        right_house = self.cleverThief(house.right)

                # left.exclusion +  right.exclusion + current house's value
        inclusion = left_house[1] + right_house[1] + house.val

                # max(left's inclusion and exclusion) + max(right's inclusion and exclusion)
        exclusion = max(left_house) + max(right_house)

        return (inclusion, exclusion)

    def rob(self, root) -> int:
        inclusion, exclusion = self.cleverThief(root)

        return max(inclusion, exclusion)
        