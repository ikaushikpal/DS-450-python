def longestString(arr, n, k):
    hashMap = {}
    i = j = 0
    max_window = -1


    while j < n:
        char = arr[j]
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
        
        if len(hashMap) < k:
            j += 1
        
        elif len(hashMap)  == k:
            max_window = max(max_window, j-i+1)
            j += 1
        
        elif len(hashMap)  > k:
            while len(hashMap) > k:
                char = arr[i]
                if char not in hashMap:
                    break

                hashMap[char] -= 1
                if hashMap[char] == 0:
                    del hashMap[char]
                i += 1
                
            max_window = max(max_window, j-i+1)
            j += 1
                
    return max_window


def pickToys(toys):
    return longestString(toys, len(toys), 2)


if __name__ == '__main__':
    toys = 'abaccab'
    print(pickToys(toys))
    