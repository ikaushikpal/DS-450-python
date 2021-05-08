from collections import deque


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def areAnagrams(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False

    q1 = deque()
    q2 = deque()
    q1.append(root1)
    q2.append(root2)
    hashMap = {}

    while len(q1) and len(q2):
        hashMap = {}
        n1 = len(q1)
        n2 = len(q2)

        if n1 != n2:
            return False

        while n1:
            current_node_left = q1.popleft()
            data = current_node_left.data
            if data not in hashMap:
                hashMap[data] = 1
            else:
                hashMap[data] += 1

            if current_node_left.left:
                q1.append(current_node_left.left)
            if current_node_left.right:
                q1.append(current_node_left.right)
            n1 -= 1

        count = len(hashMap)

        while n2:
            current_node_right = q2.popleft()
            data = current_node_right.data

            if data not in hashMap:
                return False
            else:
                hashMap[data] -= 1
                if hashMap[data] == 0:
                    count -= 1

            if current_node_right.left:
                q2.append(current_node_right.left)
            if current_node_right.right:
                q2.append(current_node_right.right)
            n2 -= 1

        if count != 0:
            return False

    return True


if __name__ == "__main__":
    root1 = newNode(1)
    root1.left = newNode(3)
    root1.right = newNode(2)
    root1.right.left = newNode(5)
    root1.right.right = newNode(4)

    root2 = newNode(1)
    root2.left = newNode(2)
    root2.right = newNode(3)
    root2.left.left = newNode(4)
    root2.left.right = newNode(5)

    if areAnagrams(root1, root2):
        print("Yes")
    else:
        print("No")
