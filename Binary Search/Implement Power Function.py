class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        result = 1
        while (n > 0):
            if (n % 2 == 0):
                x = x * x;
                n = n // 2;

            else:
                result = result * x;
                n = n - 1;
    
        if result < 0:
            return abs(result+d) %d
        else:
            return result%d

x = 71045970
y =  41535484
d =  64735492

print(Solution().pow(x, y, d))
