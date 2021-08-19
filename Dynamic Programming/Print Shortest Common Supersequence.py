class Solution:
    def longestCommonSub(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]
        output_string = ''

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i = n
        j = m

        while i and j:
            if a[i-1] == b[j-1]:
                output_string += a[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i][j-1] > dp[i-1][j]:
                    j -= 1
                else:
                    i -= 1
        output_string = output_string[::-1]

        return output_string

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        lcs = self.longestCommonSub(str1, n, str2, m)
        
        i=j=k=0
        outputString = ""

        while k < len(lcs):
            if str1[i] != lcs[k]:
                outputString += str1[i]
                i += 1
            
            elif str2[j] != lcs[k]:
                outputString += str2[j]
                j += 1
            
            elif str1[i] == lcs[k] and str2[j] == lcs[k]:
                outputString += str1[i]
                i += 1
                j+=1
                k+=1
        
        outputString += str1[i:]
        outputString += str2[j:]

        return outputString


if __name__ =='__main__':
    str1 = "abac"
    str2 = "cab"

    print(Solution().shortestCommonSupersequence(str1, str2))