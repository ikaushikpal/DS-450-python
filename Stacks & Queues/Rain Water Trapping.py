def rainWaterTrapping(arr: list) -> int:
    n = len(arr)
    maxL = [1] * n
    maxR = [1] * n

    maxL[0] = arr[0]

    for i in range(1, n):
        maxL[i] = max(maxL[i - 1], arr[i])

    maxR[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        maxR[i] = max(maxR[i + 1], arr[i])

    total_water = 0
    for i in range(n):
        total_water += min(maxL[i], maxR[i]) - arr[i]

    return total_water


if __name__ == "__main__":
    water = [3, 0, 0, 2, 0, 4]
    res = rainWaterTrapping(water)
    print(res)
