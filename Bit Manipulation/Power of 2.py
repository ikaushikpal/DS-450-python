class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,num):
        counter = 0

        while num:
            num = num & (num-1)
            counter += 1

        return counter == 1
