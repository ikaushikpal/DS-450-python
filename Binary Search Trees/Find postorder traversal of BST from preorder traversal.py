# Input : 40 30 35 80 100
# Output : 35 30 100 80 40

# Input : 40 30 32 35 80 90 100 120
# Output : 35 32 30 120 100 90 80 40

def convertPreToPost(preorder, size):
    if size == 0:
        return []
    
    if size == 1:
        return preorder

    postorder = []
    index = 1

    while preorder[0] >= preorder[index]:
        index += 1

    postorder.extend(preorder[index-1:0:-1])
    postorder.extend(preorder[size-1:index-1:-1])
    postorder.append(preorder[0])

    return postorder

# time complexity : O(n)
# space complexity : O(n)

if __name__ == '__main__':
    preorder = [40, 30, 35, 80, 100]
    print(convertPreToPost(preorder, len(preorder)))

    preorder = [40, 30, 32, 35, 80, 90, 100, 120]
    print(convertPreToPost(preorder, len(preorder)))
