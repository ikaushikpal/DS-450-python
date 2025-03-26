class Solution:
    def print_zigzag(self, n):
        counter = 1
        for i in range(n):
            output = [j for j in range(counter, counter+i+1, 1)]
            counter = output[-1] + 1

            if i%2:
                output = reversed(output)
            
            print('*'.join(map(str, output)))
    


if __name__ == '__main__':
    sol = Solution()
    sol.print_zigzag(5)
