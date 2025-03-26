# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

# Example 1:

# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]

# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].


from collections import deque


class FreqStack:

    def __init__(self):
        # usage for freq_stack:
        # here we store stack for each freqency
        # for example
        # 1 : [5, 7, 4]
        # 2: [5, 7]
        # 3: [5]
        # meaing is this that for frequency of 3 we have 5, so on 
        # why this ? because we need pop from stack and also this will help
        # to maintain the poping order that always pop from top if having freq same
        # and need to do in O(1)
        self.freq_stack = {}
        # usage for value_freq:
        # here we store freqency for each value that are in present in stack
        self.value_freq = {}
        # we need to pop from most frequent element thats why maxFreq will keep track
        # of maximum frequency of any value
        self.maxFreq = 0

    def push(self, val: int) -> None:
        # initial frequency of all values
        freq = 1

        # if value already exist in stack
        if val in self.value_freq:
            freq += self.value_freq[val]
        # incremented frequency or new frequency
        self.value_freq[val] = freq

        # if this value's frequency is new highest
        # then need to add this value to new stack of that frequency
        if freq > self.maxFreq:
            self.freq_stack[freq] = deque([val])
            # updating maxFreq
            self.maxFreq = freq
        # if this value's frequency is less than or equal to maxFreq
        # then no need of new freq stack, simply push
        else:
            self.freq_stack[freq].append(val)

    def pop(self) -> int:
        # popping from maxFreq stack
        popped = self.freq_stack[self.maxFreq].pop()

        # if len of maxFreq stack is empty then delete it
        if len(self.freq_stack[self.maxFreq]) == 0:
            del self.freq_stack[self.maxFreq]
            self.maxFreq -= 1 # update maxFreq
            
        # also need to decrement popped values frequency
        self.value_freq[popped] -= 1
        # if popped values frequency is 0 that means it is useless to
        # keep in out dict, delete it
        # even if this value later occurred then we will add it that time
        if self.value_freq[popped] == 0:
            del self.value_freq[popped]

        return popped


if __name__ == '__main__':
    fs = FreqStack()
    print(fs.push(5))
    print(fs.push(7))
    print(fs.push(5))
    print(fs.push(7))
    print(fs.push(4))
    print(fs.push(5))
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
