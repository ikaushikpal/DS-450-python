# You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

# For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

# Implement the TopVotedCandidate class:

# TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
# int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
 

# Example 1:

# Input
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
# [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
# Output
# [null, 0, 1, 1, 0, 0, 1]

# Explanation
# TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
# topVotedCandidate.q(3); // return 0, At time 3, the votes are [0], and 0 is leading.
# topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
# topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# topVotedCandidate.q(15); // return 0
# topVotedCandidate.q(24); // return 0
# topVotedCandidate.q(8); // return 1


import bisect
from collections import Counter
from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        votingMachine = Counter()
        self.times = times
        self.leadingPerson = []
        leading = persons[0]
        
        for person in persons:
            votingMachine[person] += 1   
            if votingMachine[person] >= votingMachine[leading]:
                leading = person
                
            self.leadingPerson.append(leading)
    # Time Complexity : O(N)
    # Space Complexity: O(N)

    def q(self, t: int) -> int:
        floorIndex = bisect.bisect_right(self.times, t) - 1
        return self.leadingPerson[floorIndex]
    # Time Complexity : O(logN)
    # Space Complexity: O(1)  

# Overall Time Complexity: O(QlogN) + O(N)
# Overall Space Complexity: O(N)


if __name__ == "__main__":
    # Your TopVotedCandidate object will be instantiated and called as such:
    obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    param_1 = obj.q(3)
    param_2 = obj.q(12)
    param_3 = obj.q(25)
    param_4 = obj.q(15)
    param_5 = obj.q(24)
    param_6 = obj.q(8)