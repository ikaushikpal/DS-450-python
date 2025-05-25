class Solution:
    def is_bit_set(self, n, i):
        mask = 1 << i
        return (n & mask) != 0

    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def set_ith_bit(self, n, i):
        mask = 1 << i
        return n | mask

    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def clear_ith_bit(self, n, i):
        mask = 1 << i
        mask = ~mask
        return n & mask

    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def toggle_ith_bit(self, n, i):
        mask = 1 << i
        mask = ~mask
        return n ^ mask

    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def remove_last_set_bit(self, n):
        mask = n - 1
        return n & mask

    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def is_power_of_2(self, n):
        mask = n - 1
        return (n & mask) == 0

    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def count_set_bits(self, n):
        # approach 1
        # count = 0
        # while n:
        #     count += n & 1
        #     n = n >> 1
        # return count

        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count


# Time Complexity: O(32) = O(1)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.is_bit_set(13, 3))
    print(sol.set_ith_bit(13, 3))
    print(sol.clear_ith_bit(13, 3))
    print(sol.toggle_ith_bit(13, 3))
    print(sol.remove_last_set_bit(13))
    print(sol.is_power_of_2(13))
    print(sol.count_set_bits(13))