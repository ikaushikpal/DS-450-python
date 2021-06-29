class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        counter = 0
        while a and b:
            if a&1 != b&1:
                counter += 1

            a >>= 1
            b >>= 1

        while a:
            if a&1:
                counter += 1
            a >>= 1

        while b:
            if b&1:
                counter += 1
            b >>= 1

        return counter 

if __name__ == '__main__':
    sol = Solution()
    print(sol.countBitsFlip(3, 1))