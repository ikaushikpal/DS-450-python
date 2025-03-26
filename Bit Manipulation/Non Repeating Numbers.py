class Solution:
	def singleNumber(self, nums):
		# Code here
		axorb = 0
		for num in nums:
		    axorb = axorb ^ num
        
        rsbmsk = axorb & -axorb
        
        a = 0
        b = 0
        
        for val in nums:
            if val & rsbmsk == 0:
                a = a ^ val
            else:
                b = b ^ val
        
        if a > b :
            return b , a
        else: 
            return a , b
