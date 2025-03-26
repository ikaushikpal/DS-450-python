class Solution:
    def find_saddle_point(self, matrix) -> int:
        # first need to find lowest value in each row
        # then it may be a saddle point, then check that column if that element is the maximum in column
        # if yes, then it is a saddle point
        # it is not gurrented that every matrix will have a saddle point
        # if no saddle point is fount then return -1
        # saddle point is that element which is min in that row and max in that column

        m, n = len(matrix), len(matrix[0])

        for i, row in enumerate(matrix, 0):
            FLAG = True
            lowest_value = float('inf')
            index = 0
            for j, ele in enumerate(row, 0):
                if ele < lowest_value:
                    lowest_value = ele
                    index = j
            
            # check if saddle
            for k in range(m):
                if matrix[k][index] > lowest_value:
                    FLAG = False
                    break
            
            if FLAG:
                return lowest_value
        return -1


if __name__ == '__main__':
   
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    print(Solution().find_saddle_point(mat))
 