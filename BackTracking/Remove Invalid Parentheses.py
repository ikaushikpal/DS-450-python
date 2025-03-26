# using DFS backtracking
class Solution:
    def __init__(self, parenthesis):
        self.parenthesis = parenthesis
        self.N = len(parenthesis)
    
    def isParenthesis(self, char):
	    return ((char == '(') or (char == ')'))

    def isValidString(self, str):
        cnt = 0
        for i in range(len(str)):
            if (str[i] == '('):
                cnt += 1
            elif (str[i] == ')'):
                cnt -= 1
            if (cnt < 0):
                return False
        return (cnt == 0)
    
    def getValidStringUtil(self, str, length, x):
        if length == self.N - 1:
            if str not in self.mySet and self.isValidString(str):
                print(str)
                self.mySet.add(str)

            return

        if (length and str[0] == ')') or x >= self.N:
            return
        
        while x < self.N and not self.isParenthesis(self.parenthesis[x]):
            str += self.parenthesis[x]
            length += 1
            x += 1

        self.getValidStringUtil(str + self.parenthesis[x], length+1, x+1)
        self.getValidStringUtil(str, length, x+1)
    

    def getValidString(self):
        self.mySet = set()
        self.getValidStringUtil('', 0, 0)

class BFS:
    def isParenthesis(self, char):
	    return ((char == '(') or (char == ')'))

    def isValidString(self, str):
        cnt = 0
        for i in range(len(str)):
            if (str[i] == '('):
                cnt += 1
            elif (str[i] == ')'):
                cnt -= 1
            if (cnt < 0):
                return False
        return (cnt == 0)

    def removeInvalidParenthesis(self, str):
        if (len(str) == 0):
            return
		
        visit = set()
        
        q = []
        temp = 0
        level = 0
        
        q.append(str)
        visit.add(str)

        while(len(q)):

            str = q[0]
            q.pop()
            
            if (self.isValidString(str)):
                print(str)
                level = True

            if (level):
                continue

            for i in range(len(str)):
                if (not self.isParenthesis(str[i])):
                    continue

                temp = str[0:i] + str[i + 1:]

                if temp not in visit:
                    q.append(temp)
                    visit.add(temp)


if __name__ == '__main__':
    s = Solution('()v)')
    s.getValidString()

    s1 = Solution('()())()')
    s1.getValidString()

	