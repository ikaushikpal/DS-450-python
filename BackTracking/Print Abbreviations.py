class Solution:
    def print_abbreviations(self, string:str) -> None:
        self.print_abbreviations_util(string, '', 0)

    def print_abbreviations_util(self, string:str, abbreviation:str, count:int) -> None:
        # base case
        if len(string) == 0:
            if count > 0:
                print(f"{abbreviation}{count}")
            else:
                print(f"{abbreviation}")

            return

        current_char = string[0]

        # first add current char
        # check if leading zero count is zero or not
        if count == 0:
            self.print_abbreviations_util(string[1:], abbreviation+current_char, 0)
        else:
            self.print_abbreviations_util(string[1:], abbreviation+str(count)+current_char, 0)
        

        # now exclude current char
        self.print_abbreviations_util(string[1:], abbreviation, count + 1)



if __name__ == '__main__':
    sol = Solution()
    sol.print_abbreviations('pep')