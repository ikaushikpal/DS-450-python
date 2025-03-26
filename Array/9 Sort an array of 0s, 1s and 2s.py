class Solution:
    def sort012(self, arr, n):
        if len(arr) <= 1:
            return arr

        zero = one = two = 0
        for val in arr:
            if val == 0:
                zero += 1
            elif val == 1:
                one += 1
            else:
                two += 1

        for i in range(n):
            if zero:
                arr[i] = 0
                zero -= 1
            elif one:
                arr[i] = 1
                one -= 1
            else:
                arr[i] = 2
                two -= 1
        return arr

    def sort012V2(self, arr, n):
        if len(arr) <= 1:
            return arr

        low = mid = 0
        high = n-1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1

            elif arr[mid] == 1:
                mid += 1

            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr


if __name__ == "__main__":
    arr = [2, 0, 1, 0, 2]
    n = len(arr)

    sol = Solution()
    res = sol.sort012V2(arr, n)

    print(res)
