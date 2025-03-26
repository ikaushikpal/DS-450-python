from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count_camers = [layer.count('1') for layer in bank]
        prev_layer_count = 0
        count = 0

        for current_layer_count in count_camers:
            if current_layer_count > 0:
                count += current_layer_count * prev_layer_count
                prev_layer_count = current_layer_count

        return count


if __name__ == '__main__':
    bank = ["011001","000000","010100","001000"]
    sol = Solution()

    print(sol.numberOfBeams(bank))