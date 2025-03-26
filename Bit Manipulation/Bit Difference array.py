class Solution:   
    def countBits(self, n, arr):
        counter = 0
        MOD = (10**9) + 7
        
        while True:
            count_0 = 0
            count_1 = 0
            flag = 0

            for i in range(n):
                if arr[i] & 1 == 0:
                    count_0 += 1
                else:
                    count_1 += 1
                
                arr[i] = arr[i] >> 1

                if arr[i] == 0:
                    flag += 1
            
            counter += (count_0 * count_1 * 2)

            if flag == n:
                break
        
        return counter%MOD