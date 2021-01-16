# Josephus Problem | Game of Death in a circle | Execution in Circle

def JosephusProblem(n, k):
    arr = [x+1 for x in range(n)]
    res = JosephusProblemUtil(0, arr, k)
    return res

def JosephusProblemUtil(start_index, array, k):
    if len(array) == 1:
        return array[0]
    
    kill_index = (start_index + k -1) % len(array)
    array.pop(kill_index)
    return JosephusProblemUtil(kill_index, array, k)


alive_no = JosephusProblem(40, 7)
print(alive_no)