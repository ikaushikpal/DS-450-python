class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, num):
        counter = 0

        while num:
            num = num & (num-1)
            counter += 1

        return counter