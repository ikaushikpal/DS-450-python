# generic template
# =================================================================
import io,os,sys


buffer = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


def inputString()->str:
    '''Can be used to take fast input from commandline.
    Only Use for online test cases like geeksforgeeks, hackerrank, codechef etc
    '''
    return buffer().decode()



def printInt(value:int)->None:
    '''Use to print int type variables
    '''
    sys.stdout.write(str(value) + "\n")



def printFloat(value:float)->None:
    '''Use to print float type variables
    '''
    sys.stdout.write(str(value) + "\n")



def printString(string:str)->None:
    '''Use to print string type variables
    '''
    sys.stdout.write(string + "\n")



def printArray(array:list)->None:
    '''Use to print array equivalent code is print(*array)
    '''
    sys.stdout.write(" ".join(map(str, array)) + "\n")
# ===================================================================

class Solution:


    def countSubarray(self,arr, n, k):
        dp = [0] * n
        MAX = 10 **9 + 7
        prevIndex = MAX
        
        if arr[0] > k:
            dp[0] = 1
        else:
	        prevIndex = 0
	    
        for i in range(1, n):
            if arr[i] > k:
                
                if arr[i-1] > k:
                    dp[i] = dp[i-1] + 1
                    
                else:
                    dp[i] = dp[i-1] + (i-prevIndex) + 1
                prevIndex = MAX
            
            else:
                dp[i] = dp[i-1]
                prevIndex = min(prevIndex, i)
        
        return sum(dp)

Solution().countSubarray([30, 4, 26, 6], 4, 16)