# You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

# Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

# At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

# If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

# A server that is assigned task j at second t will be free again at second t + tasks[j].

# Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

# Return the array ans​​​​.

# Example 1:
# Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
# Output: [2,2,0,2,1,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 2 until second 1.
# - At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
# - At second 2, task 2 is added and processed using server 0 until second 5.
# - At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
# - At second 4, task 4 is added and processed using server 1 until second 5.
# - At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

# Example 2:
# Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
# Output: [1,4,1,4,1,3,2]
# Explanation: Events in chronological order go as follows: 
# - At second 0, task 0 is added and processed using server 1 until second 2.
# - At second 1, task 1 is added and processed using server 4 until second 2.
# - At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
# - At second 3, task 3 is added and processed using server 4 until second 7.
# - At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
# - At second 5, task 5 is added and processed using server 3 until second 7.
# - At second 6, task 6 is added and processed using server 2 until second 7.



import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # available will store the index of the server that is free
        # here we are using a min heap to store the tasks in the queue
        # key = (weight, index) because with same weight first come first serve
        available = [(server, i) for i, server in enumerate(servers)]
        # unavail will store the index of the server that is busy but can be freed at the end of the current task
        unavailable = []
        heapq.heapify(available)
        clock = 0
        res = []
        
        for i, task in enumerate(tasks):
            # advancing clock
            # need to keep in mind that there may be case where
            # clock is already advanced a lot
            clock = max(clock, i)
            
            # if there are no available servers, we need to wait until one becomes available
            # for that simply adding first free_time to clock
            if not available:
                clock = unavailable[0][0]
            
            # pop from unavailabe if any server can be free at current clock
            while unavailable and unavailable[0][0] <= clock:
                _, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
                
            # assigning task to the server with smallest weight
            server_weight, server_index = heapq.heappop(available)
            res.append(server_index)
            # free_time is the time when current server will be free
            free_time = clock + task
            # adding to unavailabe
            heapq.heappush(unavailable, (free_time, server_weight, server_index))
        
        return res


if __name__ == '__main__':
    servers = [3,3,2]
    tasks = [1,2,3,2,1,2]
    print(Solution().assignTasks(servers, tasks))
    