def minValue(s, k):
    freq = {}
    mn = 10e6
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    l = list(freq.values())
    l.sort()
    tot = 0
    mn = l[0]

    for i in range(len(l)-1, -1, -1):
        if k:
            d = l[i] - mn
            if d > k:
                l[i] -= k
                k = 0
            else:
                l[i] -= d
                k -= d

        tot += (l[i] * l[i])

    return tot


if __name__ == '__main__':
    s = 'aabcbcbcabcc'
    k = 3
    print(minValue(s, k))