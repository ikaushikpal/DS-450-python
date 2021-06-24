from collections import deque


def first_non_repeating(string):
    output = []
    hashMap = {}
    queue = deque()

    for char in string:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1

        if hashMap[char] == 1:
            queue.append(char)
        
        while len(queue):
            front = queue[0]
            if hashMap[front] > 1:
                queue.popleft()
            else:
                output.append(front)
                break
        
        if len(queue) == 0:
            output.append('#')
    return ''.join(output)



if __name__ == '__main__':
    s = 'aabc'
    print(first_non_repeating(s))
    