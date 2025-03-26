class Solution:
    def generate(self, numRows: int):    
        triangle = [[1]*x for x in range(1, numRows+1)]

        for row in range(2, numRows):
            for i in range(1, row):
                triangle[row][i] = triangle[row-1][i-1] + triangle[row-1][i]
        
        return triangle


if __name__ == '__main__':
    n = 5
    print(Solution().generate(n))