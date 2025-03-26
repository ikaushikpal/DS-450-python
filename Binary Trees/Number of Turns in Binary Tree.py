# Given a binary tree and data value of two of its nodes. Find the number of turns needed to reach from one node to another in the given binary tree.


# Example 1:
# Input:      
# Tree = 
#            1
#         /    \
#        2       3
#      /  \     /  \
#     4    5   6    7                        
#    /        / \                        
#   8        9   10   
# first node = 5
# second node = 10
# Output: 4
# Explanation: 
# Turns will be at 2, 1, 3, 6.


# Example 2:
# Input:      
# Tree = 
#            1
#         /     \
#        2        3
#      /  \      /  \
#     4    5    6    7                        
#    /         / \                        
#   8         9   10   
# first node = 1
# second node = 4  
# Output: -1
# Explanation: No turn is required since 
# they are in a straight line.



'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:

    LEFT_TURN = 0
    RIGHT_TURN = 1

    @staticmethod
    def find_common_ancestor(root, first, second):
        """
        Finds the common ancestor of given nodes.
        """
        if root is None:
            return root
        if root.data == first or root.data == second:
            # Found the target node return this node to caller
            return root
        node_found_in_left = Solution.find_common_ancestor(root.left, first, second)
        node_found_in_right = Solution.find_common_ancestor(root.right, first, second)
        if node_found_in_left and node_found_in_right:
            # Both left and right returned a node which means this node is the common ancestor
            return root
        if node_found_in_left:
            # The common ancestor was found left sub tree
            return node_found_in_left
        if node_found_in_right:
            # The common ancestor was found right right subtree
            return node_found_in_right

    @staticmethod
    def find_path(root, tgt_val, running_path, path_list):
        """
        Given a node, find the path to the target node value and
        record the path in running_path (making a copy as we go) as recursive calls are made.
        The running_path becomes the target path when the target node is found
        and is returned in the path list.
        """
        if root is None:
            return
        if root.data == tgt_val:
            # Target path found
            path_list.extend(running_path)
            return

        left_path_copy = running_path[:]
        left_path_copy.append(Solution.LEFT_TURN)
        Solution.find_path(root.left, tgt_val, left_path_copy, path_list)

        right_path_copy = running_path[:]
        right_path_copy.append(Solution.RIGHT_TURN)
        Solution.find_path(root.right, tgt_val, right_path_copy, path_list)

    def NumberOFTurns(self, root, first, second):
        if root is None:
            return 0
        if first == second:
            return 0
        # Find ancestor
        # eg:
        #          1
        #       /    \
        #       2       3
        #     /  \     /  \
        #    4    5   6    7
        #   /        / \
        #  8        9   10
        # would return 1
        ancestor = Solution.find_common_ancestor(root, first, second)

        path_to_first = []
        # Find path from ancestor to 'first'
        self.find_path(ancestor, first, [], path_to_first)
        # eg: path_to_first would have LEFT, RIGHT

        path_to_second = []
        # Find path from ancestor to second
        self.find_path(ancestor, second, [], path_to_second)
        # eg: path_to_second would have RIGHT, LEFT, RIGHT

        # Make the entire path anticlockwise so that you start from first and end up in second
        path_to_first.reverse()
        # eg: Path to first would be RIGHT, LEFT
        # Now when you combine path_to_first with the path_to_second you would have path
        # from first to second in a uniform order
        # eg: RIGHT, LEFT, RIGHT, LEFT, RIGHT
        path_to_first.extend(path_to_second)
        num_of_turns = 0
        path = path_to_first
        prev_path = path[0]
        for idx in range(1, len(path)):
            cur_path = path[idx]
            if prev_path != cur_path:
                num_of_turns += 1
            prev_path = cur_path
        return num_of_turns if num_of_turns != 0 else -1