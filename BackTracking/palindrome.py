class Solution:
# @param A : integer
# @return a list of strings
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            s = ''
            if i %3 == 0:
                s += 'Fizz'
            
            if i % 5 == 0:
                s += 'Buzz'
            
            if s == '':
                result.append(i)
            else:
                result.append(s)
        
        return result

