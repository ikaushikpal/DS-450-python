import heapq


class Solution:
    def sortedMatrix(self, n, matrix):
        mat_i, mat_j = 0, 0
        heap = []
        new_matrix = [[0]*n for _ in range(n)]

        #first push first columns elements in minHeap along with i, j value
        for i in range(n):
            ele = (matrix[i][0], i, 0)
            heapq.heappush(heap, ele)

        # now pop one element from heap and insert it in new matrix
        # and push [i, j+1] element in heap
        # repeat this process until all elements are inserted in new matrix

        while len(heap):
            val, x, y = heapq.heappop(heap)
            # inserting new element in new matrix
            new_matrix[mat_i][mat_j] = val
            mat_j += 1
            if mat_j == len(matrix[0]):
                mat_j = 0
                mat_i += 1
            
            # new push next element into heap
            if y+1 < n:
                ele = (matrix[x][y+1], x, y+1)
                heapq.heappush(heap, ele)
            
        return new_matrix


if __name__ == '__main__':
    mat = [[10,20,30,40],
        [15,25,35,45], 
        [27,29,37,48], 
        [32,33,39,50],]

    sol = Solution()
    print(sol.sortedMatrix(4, mat))