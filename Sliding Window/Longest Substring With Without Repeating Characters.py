def longestSubStringWithoutRepeating(string):
    n = len(string)
    hashMap = {}
    max_window = 0
    i = j = 0
    FLAG = False

    while j < n:
        FLAG = False
        char = string[j]

        if char not in hashMap:
            hashMap[char] = 1
            j += 1
            FLAG = True

        else:
            max_window = max(max_window, j - i)
            while string[i] != char:
                if hashMap[string[i]] == 1:
                    del hashMap[string[i]]
                i += 1
            del hashMap[char]
            i += 1

    if FLAG:
        max_window = max(max_window, j - i)

    return max_window

def longestSubStringWithoutRepeating2(string):
    n = len(string)
    hashMap = {}
    i = j = 0
    max_window = -1
    current_window = 0

    while j < n:
        current_window = j - i + 1
        char = string[j]
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
        
        if len(hashMap) > current_window:
            j += 1
        
        elif len(hashMap) == current_window:
            max_window = max(max_window, current_window)
            j += 1
        
        elif len(hashMap) < current_window:
            while len(hashMap) and len(hashMap) < current_window:
                char = string[i]
                hashMap[char] -= 1
                if hashMap[char] == 0:
                    del hashMap[char]
                i += 1

            max_window = max(max_window, current_window)
        
    return max_window

if __name__ == "__main__":
    s = "pwwkew"
    print(longestSubStringWithoutRepeating(s))

    print(longestSubStringWithoutRepeating2(s))
