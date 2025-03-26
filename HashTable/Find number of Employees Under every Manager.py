class Solution:
    def storeEmpNo(self, currentMangr, mangrEmp, res):
        if currentMangr not in mangrEmp: # lowest level employees
            res[currentMangr] = 0
            return 1

        countEmp = 0
        for employee in mangrEmp[currentMangr]:
            countEmp += self.storeEmpNo(employee, mangrEmp, res)

        res[currentMangr] = countEmp

        return countEmp + 1

    def findEmpUnder(self, empList):
        mangrEmp = {} # manager : [employees]
        ceo = None

        for employee, manager in empList:
            if manager == employee: #only case for CEO
                ceo = manager

            else: # rest
                if manager in mangrEmp:
                    mangrEmp[manager].append(employee)
                
                else: # new entry
                    mangrEmp[manager] = [employee]
        
        res = {}
        self.storeEmpNo(ceo, mangrEmp, res)

        return res

# Time Complexity : O(n)
# Space Complexity : O(n)
# where n = number of employees or managers


if __name__ == '__main__':
    t = (("A", "C"),("B", "C"),("C", "F"),("D", "E"),("E", "F"),("F", "F")) # (employee , manager)

    print(Solution().findEmpUnder(t))