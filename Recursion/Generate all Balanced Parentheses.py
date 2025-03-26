class solve:
    def __init__(self):
        self.res = []

    def generateBalancedParenthesesUtil(self, output_string, opening, closing):
        if opening == 0 and closing == 0:
            self.res.append(output_string)
            return

        if opening != 0:
            self.generateBalancedParenthesesUtil(output_string + "(", opening - 1, closing)

        if closing > opening:
            self.generateBalancedParenthesesUtil(output_string + ")", opening, closing - 1)

    def generateBalancedParentheses(self, n):
        if n == 0:
            return []
        if n == 1:
            return ["()"]

        self.generateBalancedParenthesesUtil("(", n - 1, n)
        return self.res


s = solve()
res = s.generateBalancedParentheses(4)
print(res)
