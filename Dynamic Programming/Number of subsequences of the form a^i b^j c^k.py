def countNumberSubsequence(string):
    dfa =  {0:{'a':1,'b':0,'c':0},
            1:{'a':1,'b':2,'c':0},
            2:{'a':0,'b':2,'c':3},
            3:{'a':1,'b':0,'c':3}}
    
    initial = 0
    accepting = set([3])

    state = initial # initial state
    FLAG = True
    counter = 0

    for s in string:
        state = dfa[state][s]

        if state in accepting and FLAG:
            counter += 1
            FLAG = False
        else:
            FLAG = True
    
    return counter


if __name__ == '__main__':
    s = "abcabc"
    print(countNumberSubsequence(s))
