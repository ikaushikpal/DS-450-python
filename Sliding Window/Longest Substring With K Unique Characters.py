def longestString(arr, n, k):
    hashMap = {}
    i = j = 0
    count = 0
    max_window = -1


    while j < n:
        char = arr[j]
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
        
        if hashMap[char] == 1:
            count += 1
        
        if count < k:
            j += 1
        
        elif count == k:
            max_window = max(max_window, j-i+1)
            j += 1
        
        elif count > k:
            while count > k and i < j:
                char = arr[i]
                hashMap[char] -= 1
                if hashMap[char] == 0:
                    count -= 1
                i += 1
            max_window = max(max_window, j-i+1)
            
    
    return max_window
            
    
    return max_window



if __name__ == '__main__':
    s = 'aabacbebebe'
    k = 3
    n = len(s)
    print(longestString(s, n, k))

    s = 'wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'
    n = len(s)
    k = 5
    print(longestString(s, n, k))
