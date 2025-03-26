# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False



from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    # Time Complexity : O(N)

    def pop(self) -> int:
        return self.queue.popleft()
    # Time Complexity : O(1)

    def top(self) -> int:
        return self.queue[0]
    # Time Complexity : O(1)

    def empty(self) -> bool:
        return len(self.queue) == 0
    # Time Complexity : O(1)


if __name__ == '__main__':
    myStack =MyStack()
    print(myStack.push(1))
    print(myStack.push(2))
    print(myStack.top()) # return 2
    print(myStack.pop()) # return 2
    print(myStack.empty()) # return False


