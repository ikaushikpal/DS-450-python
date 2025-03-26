def minimumWindowSubstring(string, pattern):
    n = len(string)
    hashMap = {}
    i = j = 0
    for char in pattern:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
    
    count = len(hashMap)
    minimum_window = 10e6
    output_string = ''

    while j < n:
        char = string[j]
        current_window_size = j - i +1

        if char in hashMap:
            hashMap[char] -= 1
            if hashMap[char] == 0:
                count -= 1
        
        if count == 0:
            while count == 0:
                char = string[i]
                if char in hashMap:
                    if hashMap[char] == 0:
                        break
                    hashMap[char] += 1
                i += 1            

            if minimum_window > j-i+1:
                output_string = string[i:j+1]
                minimum_window = j-i+1

        j += 1
    if output_string:
        return output_string
    return -1


if __name__ == '__main__':
    string = 'ADOBECODEBANC'
    pattern = 'ABC'
    print(minimumWindowSubstring(string, pattern))

