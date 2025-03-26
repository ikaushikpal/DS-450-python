import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        returnVal = func(*args, **kwargs)
        end = time.time()
        print(f"Total Time taken = {end-start:0.8f} ms")
        return returnVal

    return wrapper


class SolutionRec:
    def catalanUtil(self, n):
        if n <= 1:
            return 1
        
        res = 0
        for i in range(n):
            res += self.catalanUtil(i) * self.catalanUtil(n-i-1)
        
        return res

    @timer
    def catalan(self, n):
        return self.catalanUtil(n)

class SolutionMem:
    @timer
    def catalan(self, n):   
        self.dp = [0] * (n+1)
        self.dp[0] = self.dp[1] = 1

        return self.catalanUtil(n)

    def catalanUtil(self, n):
        if n <= 1:
            return 1
        
        if self.dp[n] != 0:
            return self.dp[n]

        res = 0
        for i in range(n):
            res += self.catalanUtil(i) * self.catalanUtil(n-i-1)
        
        self.dp[n] = res
        return res

class SolutionDP:
    @timer
    def catalan(self, n):   
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        
        return dp[n]
        
if __name__ == '__main__':
    # SolutionMem().catalan(1000)
    SolutionDP().catalan(5000)