import re


class Solution:
    def print_encoding(self, num:int) -> None:
        self.print_encoding_util(str(num), '')

    def print_encoding_util(self, num:str, current_encoding:str) -> None:
        if num == '0' or len(num) == 0:
            print(current_encoding)
            return

        if num[0] == '0':
            return

        self.print_encoding_util(num[1:], current_encoding + chr(ord('a') + int(num[0]) - 1))

        if len(num) >= 2 and int(num[:2]) <= 26:
            self.print_encoding_util(num[2:], current_encoding + chr(ord('a') + int(num[:2]) - 1))
    


if __name__ == '__main__':
    s = Solution()
    s.print_encoding(303)

