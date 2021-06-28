def buildPITable(pattern):
    n = len(pattern)
    pi = [0] * n

    for i in range(1, n):
        j = pi[i-1]

        while j>0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        
        if pattern[i] == pattern[j]:
            pi[i] = j+1

    return pi

def KMPAlgorithm(string, pattern):
    m = len(string)
    n = len(pattern)

    if m==0 or n == 0:
        return -1
    
    # build pi table
    piTable = buildPITable(pattern)
    i = 0
    j = 0
    res = []

    while i<m and j<n:
        FLAG = False

        if string[i] == pattern[j]:
            j += 1
            i += 1
            FLAG = True      
        else:
            j = piTable[j-1]
        
        if j == 0:
            i += 1
        
        if FLAG and j == n:
            res.append(i-n)
            j = piTable[j-1]
    
    if len(res):
        return res
    return -1


if __name__ == '__main__':
    string = 'ababcabcabababd'
    pattern = 'ababd'

    print(KMPAlgorithm(string, pattern))

    txt = "THIS IS A TEST TEXT"
    pat = "TEST"
    print(KMPAlgorithm(txt, pat))

    txt =  "AABAACAADAABAABA"
    pat =  "AABA"
    print(KMPAlgorithm(txt, pat))

    string = 'ABCAB'
    pattern = 'ABCA'
    print(KMPAlgorithm(string, pattern))
    
    print(buildPITable('ababababababab'))