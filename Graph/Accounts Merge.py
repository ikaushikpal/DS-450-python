# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

# Example 1:
# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.



# Example 2:
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]



from collections import defaultdict, namedtuple
from typing import List


class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)
        self.n += 1

    def find(self, n):
        if self.array[n] < 0:
            return (n,  -self.array[n])
        result = self.find(self.array[n])
        self.array[n] = result[0]
        return result

    def union(self, set1, set2):
        parent_of_set1, rank_of_set1 = self.find(set1)
        parent_of_set2, rank_of_set2 = self.find(set2)

        if parent_of_set1 == parent_of_set2:
            return False

        if rank_of_set1 > rank_of_set2:
            self.array[parent_of_set1] += self.array[parent_of_set2]
            self.array[parent_of_set2] = parent_of_set1

        else:
            self.array[parent_of_set2] += self.array[parent_of_set1]
            self.array[parent_of_set1] = parent_of_set2
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailPersonMap = {}
        indexEmailMap = {}
        parentIndexMap = defaultdict(list)
        result = []
        uniqueEmail = 0
        EmailPair = namedtuple('EmailPair', ['personName', 'index'])

        for account in accounts:
            person = account[0]
            for email in account[1:]:
                if email not in emailPersonMap:
                    emailPersonMap[email] = EmailPair(person, uniqueEmail)
                    indexEmailMap[uniqueEmail] = email
                    uniqueEmail += 1

        d = Disjoint(uniqueEmail)
        for account in accounts:
            for i in range(2, len(account)):
                index1 = emailPersonMap[account[i-1]].index
                index2 = emailPersonMap[account[i]].index
                d.union(index1, index2)

        for index, email in indexEmailMap.items():
            parent = d.find(index)[0]
            parentIndexMap[parent].append(email)

        for index, emails in parentIndexMap.items():
            person = [ emailPersonMap[emails[0]].personName ]
            result.append(person + sorted(emails))

        return result
# Really HARD one
# Time Complexity : O(N) + O(NLogN) = O(NlogN) because of sorting
# Space Complexity : O(unique emailIds) = O(N)
# where N is the len(accounts)


if __name__ == '__main__':
    sol = Solution()
    print(sol.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                                      ["John", "johnsmith@mail.com",
                                       "john00@mail.com"],
                                      ["Mary", "mary@mail.com"],
                                      ["John", "johnnybravo@mail.com"]]))

    print(sol.accountsMerge(accounts=[["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], [
          "Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
