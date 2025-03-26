def solve(nums, n):
    tot = i = 0
    while i < n:
        ele = nums[i]
        if ele < 0:
            while i < n and nums[i] < 0:
                ele = max(ele, nums[i])
                i += 1
        else:
            while i < n and nums[i] >= 0:
                ele = max(ele, nums[i])
                i += 1
        tot += ele
    return tot


n = int(input())
nums = list(map(int, input().split()))
print(solve(nums, n))