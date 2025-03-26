def Push(x, stack1, stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    if len(stack1) == 0:
        stack1.append(x)
    else:
        # first pop from stack1 and push into stack2
        # it will reverse stack1 in stack2
        while len(stack1):
            popped_value = stack1.pop()
            stack2.append(popped_value)

        stack1.append(x) # inserting main value
        # x will be at bottom

        # again pop from stack2 and push into stack1
        # it will give back to original stack1
        while len(stack2):
            popped_value = stack2.pop()
            stack1.append(popped_value)


def Pop(stack1,stack2):
    if len(stack1) == 0:
        return -1
    
    return stack1.pop()



# in this method pushing will be costly O(n)
# because we are exhausting stack1 twice 
# Push will cost f(n) = 2*n + 1
# Best case is constant Ω(1)
# Worst Case O(n)
# Avg Case Θ(n)

# For Pop Code it is only checking if it is empty or not otherwise normal pop
# f(n) = 1
# Avg Case Θ(1) ≈ Constant
 
