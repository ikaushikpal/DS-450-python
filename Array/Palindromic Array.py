# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

 

# Example:
# Input:
# 2
# 5
# 111 222 333 444 555
# 3
# 121 131 20

# Output:
# 1
# 0

# Explanation:
# For First test case.
# n=5;
# A[0] = 111    //which is a palindrome number.
# A[1] = 222   //which is a palindrome number.
# A[2] = 333   //which is a palindrome number.
# A[3] = 444  //which is a palindrome number.
# A[4] = 555  //which is a palindrome number.
# As all numbers are palindrome so This will return 1.


# Constraints:
# 1 <=T<= 50
# 1 <=n<= 20
# 1 <=A[]<= 10000

def PalinArray(arr, n):
    def reverse(num):
        newNum = 0
        while num:
            rem = num % 10
            newNum = newNum * 10 + rem
            num = num // 10
        return newNum
    
    for num in arr:
        if num != reverse(num):
            return False
    return True
# Time Complexity : (10000 * n) = O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    print(PalinArray([111, 222, 333, 444, 555]))