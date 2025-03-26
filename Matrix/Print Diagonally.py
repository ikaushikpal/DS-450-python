def downwardDigonal(n, A): 
    res = []
    for i in range(n):
        for j in range(i, -1, -1):
            res.append(A[i-j][j])
        
    for i in range(1, n, 1):
        k = i
        for j in range(n-1, i-1, -1):
            res.append(A[k][j])
            k += 1
    
    return res
    


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(downwardDigonal(4, matrix))