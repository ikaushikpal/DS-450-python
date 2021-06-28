BASE = 256
# we are taking 256 as base meaning
# all ASCII characters are allowed in this algorithm


def buildHashValue(patten):
    n = len(patten)
    if n == 0:
        return 0

    hashValue = 0
    for i in range(n):
        asciiValue = ord(patten[i])
        power = n - i - 1

        hashValue += asciiValue * (BASE ** power)

    return hashValue


def calcRollingHash(string, stringHash, i, n):
    rollingHashPower = n - 1

    lastCharASCIIValue = ord(string[i - n])
    newCharASCIIValue = ord(string[i])

    stringHash = stringHash - (lastCharASCIIValue * (BASE ** rollingHashPower))
    stringHash = stringHash * BASE
    stringHash += newCharASCIIValue

    return stringHash


def rabinKarpAlgorithm(string, patten):
    n = len(patten)
    m = len(string)

    if (
        n == 0 or m == 0 or n > m
    ):  # if pattern size is higher than string then noway we will find
        return -1  # pattern in string

    allPOS = []  # for storing all occurrences

    # calculating pattern hashValue
    patternHash = buildHashValue(patten)
    stringHash = 0  # Initializing value

    # calculating first n-characters hash value
    # with this hashvalue we will modify it
    for i in range(n):
        asciiValue = ord(string[i])
        power = n - i - 1

        stringHash += asciiValue * (BASE ** power)

    for i in range(n, m):
        if stringHash == patternHash:
            # checking if subString from i-n to i is same with n
            # then just append res, if we want only first then instead of appending
            # just directly return i-n
            if string[i - n : i] == patten:
                # if we found a valid pattern in string
                allPOS.append(i - n)

                # recalculating stringHash value
                # if "ab.a" if we calculated then
                # subtract previous a * (base *power) then with result multiply with base
                # finally add current ith character's ASCII with res
        stringHash = calcRollingHash(string, stringHash, i, n)
        # Formula : (stringHash - prevChar * (BASE ** (n-1))* BASE + currentChar

    # checking if last subString is same with pattern or not
    # because our for will terminate so we cannot check last time
    if stringHash == patternHash:
        if string[m - n : m] == patten:
            allPOS.append(m - n)

    if len(allPOS):
        return allPOS
    else:
        return -1


if __name__ == "__main__":
    string = "THIS IS A TEST TEXT"
    pattern = "TEST"
    print(rabinKarpAlgorithm(string, pattern))

    string = "AABAACAADAABAABA"
    pattern = "AABA"
    print(rabinKarpAlgorithm(string, pattern))

    string = "ABAB"
    pattern = "AB"
    print(rabinKarpAlgorithm(string, pattern))

# TimeComplexity = O(n) [for calculating patternHash] + O(n) [for calculating stringHash]
# + O(m-n+1) [for traversing and calculating string and it's hash]
#          1 because we are checking outside of loop once
# final Time Complexity = O(n + n + m-n+1) = O(m+n) {avg}
# but it worst case O(m*n)
# space complexity = O(1)
