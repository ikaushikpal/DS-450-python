from collections import deque


class Solution:
    @classmethod
    def siblingSearch(cls, N, arr, target):
        if len(arr) == 0:
            return [-1]
        
        if arr[0] == target:
            return [-1]

        queue = deque()
        queue.append(0)

        while queue:
            levelCopy = queue.copy()
            for _ in range(len(queue)):
                curr = queue.popleft()

                if arr[curr] == target:
                    temp = [arr[index] for index in levelCopy if arr[index] != target]
                    return sorted(temp) if len(temp) > 0 else [-1]

                if curr * 2 + 1 < N:
                    queue.append(curr * 2 + 1)

                if curr * 2 + 2 < N:
                    queue.append(curr * 2 + 2)
        return [-1]


if __name__ == '__main__':
    sol = Solution()
    print(Solution.siblingSearch(6, [1, 2, 3, 4, 5, 6], 5))