class Solution:
    def print_lexical_ordering(self, n:int) -> None:
        self.print_lexical_ordering_helper(n, '')

    def print_lexical_ordering_helper(self, n:int, current_prefix:str) -> None:
        if current_prefix != '':
            print(current_prefix)

        start = 1 if len(current_prefix) == 0 else 0
        end = 9

        for i in range(start, end+1):
            num = f'{current_prefix}{i}'
            
            if int(num) > n:
                return

            self.print_lexical_ordering_helper(n, num)



if __name__ == '__main__':
    sol = Solution()
    sol.print_lexical_ordering(100)