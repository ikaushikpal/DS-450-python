class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
    def intersect(self, A, B):
        ptr1 = ptr2 = 0
        n1, n2 = len(A), len(B)

        C = []
        while ptr1< n1 and ptr2<n2:
            if ptr1< n1 and ptr2<n2 and A[ptr1] == B[ptr2]:
                while ptr1< n1 and ptr2<n2 and A[ptr1] == B[ptr2]:
                    C.append(A[ptr1])
                    ptr1 += 1
                    ptr2 += 1
            
            elif A[ptr1] > B[ptr2]:
                ptr2 += 1
            
            elif A[ptr1] < B[ptr2]:
                ptr1 += 1

        return C


if __name__ == '__main__':
    arr1 = [1, 2, 3, 3, 4, 5, 6]
    arr2 = [3, 3, 5]

    print(Solution().intersect(arr1, arr2))
        


