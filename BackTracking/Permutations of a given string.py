class Solution:
    def find_permutation(self, S):
        S = sorted(S)
        self.res = []
        visited = [False] * len(S)
        self.find_permutationUtil(S, visited, '')
        return self.res

    def find_permutationUtil(self, S, visited, str):
        if len(str) == len(S):
            self.res.append(str)
            return
        
        for i in range(len(S)):
            char = S[i]
            if visited[i] == False:
                visited[i] = True
                self.find_permutationUtil(S, visited, str+char)
                visited[i] = False


if __name__ == '__main__':
    sol = Solution()
    sol.find_permutation("ABC")
