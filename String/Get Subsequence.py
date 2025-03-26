class Solution:
    def get_subsequence(self, str):
        if len(str) == 0:
            return ['']
        
        output = self.get_subsequence(str[1:])
        result = [str[0]+ s for s in output]

        return output + result


if __name__ == '__main__':
    s = Solution()
    print(s.get_subsequence('abc'))