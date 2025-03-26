class Solution:
    def longestUniqueSubsttr(self, string:str)->int:
        maxLength = 0
        unique = {}
        j = 0

        for i in range(len(string)):
            if string[i] in unique:
                # found duplicates
                unique[string[i]] += 1

                while unique[string[i]] != 1:
                    unique[string[j]] -= 1

                    if unique[string[j]] == 0:
                        del unique[string[j]]

                    j += 1
            else:
                unique[string[i]] = 1

            maxLength = max(maxLength,len(unique))

        return maxLength

if __name__ == '__main__':
    print(Solution().longestUniqueSubsttr("geeksforgeeks"))
    print(Solution().longestUniqueSubsttr("abdefgabef"))
    print(Solution().longestUniqueSubsttr("BBBB"))