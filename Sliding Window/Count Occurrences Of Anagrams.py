def countOccurrencesAnagram(string, pattern):
    n = len(string)
    k = len(pattern)

    i = j = count_anagram = 0
    hashMap = {}

    for char in pattern:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1

    count = len(hashMap)

    while j < n:
        if string[j] in hashMap:
            hashMap[string[j]] -= 1

            if hashMap[string[j]] == 0:
                count -= 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if count == 0:
                count_anagram += 1

            if string[i] in hashMap:
                hashMap[string[i]] += 1

                if hashMap[string[i]] == 1:
                    count += 1
            i += 1
            j += 1

    return count_anagram


if __name__ == "__main__":
    s = "aabaabaa"
    p = "aaba"
    res = countOccurrencesAnagram(s, p)
    print("Total No of Anagrams present in the main string =", res)

    s = "forxxorfxdofr"
    p = "for"
    res = countOccurrencesAnagram(s, p)
    print("Total No of Anagrams present in the main string =", res)
