# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.

 
# Example 1:
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.


# Example 2:
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.


from collections import Counter
import heapq
from math import ceil
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        maxHeap = [-value for value in Counter(arr).values()]
        heapq.heapify(maxHeap)
        ans, remaining = 0, len(arr)
        while len(maxHeap) > 0 and remaining > len(arr) // 2:
            remaining += heapq.heappop(maxHeap)
            ans += 1
        return ans
# Time Complexity: O(NlogN)
# Space Complexity: O(N)

# ✔️ Solution - III (Find Frequency and Bucket Sort)

# Instead of sorting the frequency of elements, we could use bucket sort over the range [0, 100000] since the frequency of elements always fall within this range. This will reduce the sorting time from O(NlogN) to O(N). The steps used in this approach are as follows -

# Find the frequency of elements in arr. Here, freq array is used, where freq[i] will denote frequency of element i. Use hashmap to generalize for any arr[i] but array works here since 1 <= arr[i] <= 100000

# Find the count (or frequency) of each frequency. Here freqBuckets is used, where freqBucket[i] will denote the number of elements in arr having frequency i.

# Keep deleting all elements of a given frequency till atleast half are deleted. We start from max possible frequency i=100000.
# If instances of frequency i is present (i.e freqBuckets[i] > 0) then delete an instance of that frequency. Repeat till all elements of this frequency are deleted or array size is reduced by half or .

# ans will be incremented each time an instance of a frequency is deleted.

# Another optimization I have used here is instead of deleting an instance one-by-one, we can simply find the number of instances of a frequency to delete (denoted by noOfFreqToDelete) in O(1). We can either delete all instances of a frequency or only as much required to get array size to half.
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        freqBuckets, maxFreq = {}, 0
        for value in freq.values():
            freqBuckets[value] = 1 + freqBuckets.get(value, 0)
            maxFreq = max(maxFreq, value)
        
        ans, deleteRequired, i = 0, len(arr) >> 1, maxFreq
        while deleteRequired > 0:
            if freqBuckets.get(i, 0) > 0:
                noOfFreqToDelete = min(freqBuckets[i], ceil(deleteRequired / i))
                deleteRequired -= noOfFreqToDelete * i
                ans += noOfFreqToDelete
            i -= 1
        return ans
# Time Complexity: O(N)
# Space Complexity: O(100000) = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSetSize([3,3,3,3,5,5,5,2,2,7]))
    print(sol.minSetSize([7,7,7,7,7,7]))
    print(sol.minSetSize([1,2,3,4,5,6,7,8,9,10]))
        