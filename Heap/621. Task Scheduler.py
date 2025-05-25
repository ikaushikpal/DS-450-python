# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.


# Constraints:
# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100


from collections import deque
import heapq
from typing import Counter, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        max_heap = [-value for value in c.values()]
        queue = deque()
        
        time = 0
        while queue or max_heap:
            time += 1

            if max_heap:
                freq = heapq.heappop(max_heap)

                if freq < -1:
                    queue.append((freq + 1, time + n))
            
            if queue and queue[0][1] <= time:
                freq, _ = queue.popleft()
                heapq.heappush(max_heap, freq)
            
            if not max_heap and queue and queue[0][1] > time:
                time = queue[0][1] - 1
                freq, _ = queue.popleft()
                heapq.heappush(max_heap, freq)
        return time

        



if __name__ == '__main__':
    sol = Solution()
    print(sol.leastInterval(["B","C","D","A","A","A","A","G"], 1))
    print(sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
    print(sol.leastInterval(tasks = ["A","A","A"], n = 1))