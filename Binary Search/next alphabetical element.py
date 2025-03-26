# Smallest alphabet greater than a given character

# Given a list of sorted characters consisting of both Uppercase and Lowercase Alphabets and a particular target value, say K, the task is to find the smallest element in the list that is larger than K. 
# Letters also wrap around. For example, if K = ‘z’ and letters = [‘A’, ‘r’, ‘z’], then the answer would be ‘A’.

# Examples:  

# Input : Letters = ["D", "J", "K"]
#         K = "B"
# Output: 'D'
# Explanation:
# The Next greater character of "B" is 'D'
# since it is the smallest element from the 
# set of given letters, greater than "B".

# Input:  Letters = ["h", "n", "s"]
#         K = "t"
# Output: 'h'

def nextAlphabeticalElement(s, n, key):
    if s[n-1] <= key: return None

    low, high = 0, n-1
    res = None
    
    while low <= high:
        mid = (low+high) // 2

        if s[mid] == key: return s[mid+1]

        elif s[mid] > key:
            res = s[mid]
            high = mid - 1
        else:
            low = mid + 1
    
    return res


s = ["a", "c", "f", "h"]
key = 'b'

print(nextAlphabeticalElement(s, len(s), key))