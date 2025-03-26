# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 
# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


from typing import List


class Solution:
    def restoreIpAddressesUtil(self, ip, remaining, s, ans):
        # base case
        if remaining>len(s) or len(s)>remaining*3:
            return
        
        # if all octate found
        if remaining == 0:
            # check if input s is fully utilized
            if len(s) == 0:
                ans.append(ip[1:])
            return

        # octate can have maximum 3 digit [255]
        for i in range(3):
            if len(s) > i:
                octate = s[:i+1]
                striped_leading_zeros = octate.lstrip('0')
                
                # octate is valid only if its value if in range [0, 255]
                # and no leading zero like 012 or 015, only leading zero is allowed
                # if octate is '0' itself which is valid
                if 0<=int(octate)<=255 and (len(striped_leading_zeros) == len(octate) or octate == '0'):
                    self.restoreIpAddressesUtil(f'{ip}.{octate}', remaining-1, s[i+1:], ans)
            
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.restoreIpAddressesUtil('', 4, s, ans)
        return  ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreIpAddresses('0000'))
    print(sol.restoreIpAddresses('25525511135'))
    print(sol.restoreIpAddresses('101023'))
