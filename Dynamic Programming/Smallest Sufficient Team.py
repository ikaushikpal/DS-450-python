# In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

# Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

# For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
# Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

# It is guaranteed an answer exists.

 
# Example 1:
# Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]


# Example 2:
# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]


from typing import List


class Solution:
    def generateMap(self, req_skills):
        return {skill:i for i, skill in enumerate(req_skills)}
    
    def mapSkill(self, skills, skillMaper):
        rep = 0
        for skill in skills:
            pos = skillMaper[skill]
            rep |= (1 << pos)
        return rep
    
    def dfs(self, index, currSkill, finalSkill, peopleReq):
        if currSkill == finalSkill and len(peopleReq) < self.minimumPeople:
            self.minimumPeople = len(peopleReq)
            self.seq = peopleReq[:]
            return
        
        if index == len(self.peopleSkills):
            return
        
        if len(peopleReq) >= self.minimumPeople:
            return
        
        if currSkill in self.skillsSeen:
            return
        
        self.dfs(index + 1, currSkill, finalSkill, peopleReq)
        newCurrSkill = currSkill | self.peopleSkills[index]
        peopleReq.append(index)
        self.dfs(index + 1, newCurrSkill, finalSkill, peopleReq)
        peopleReq.pop()
        
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillMaper = self.generateMap(req_skills)
        self.peopleSkills = [self.mapSkill(p, skillMaper) for p in people]
        
        self.minimumPeople = float('inf')
        self.seq = []
        self.skillsSeen = set()
        finalSkill = (1 << len(req_skills)) - 1
        self.dfs(0, 0, finalSkill, [])
        
        return self.seq
# NOT COMPETED
# TIME LIMIT EXCEEDED

if __name__ == '__main__':
    sol = Solution()
    req_skills = ["java","nodejs","reactjs"]
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    print(sol.smallestSufficientTeam(req_skills, people))

    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    print(sol.smallestSufficientTeam(req_skills, people))