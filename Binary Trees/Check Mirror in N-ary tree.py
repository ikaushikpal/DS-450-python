class Solution:
    def checkMirrorTree(self, n, e, A, B):
        if n==1:
            return A[0] == B[0]
        
        previndex = 1
        level = 1
        i = 1
        j = min(2*e, (2**(level+1)) + previndex) - 1

        while 1:
            temp = j
            limit = j//2 + 1

            while i <= limit:
                if A[i] != B[j]:
                    return 0
                
                i += 2
                j -= 2

            if temp == 2*e - 1:
                break

            previndex = temp+1
            i = previndex
            j = min(2*e, (2**(level+1)) + previndex) - 1
            level += 1

        return 1


if __name__ == '__main__':
    A = [1, 2, 1 ,3]
    B = [1, 3, 1 ,2]
    n, e = 3, 2

    print(Solution().checkMirrorTree(n, e, A, B))