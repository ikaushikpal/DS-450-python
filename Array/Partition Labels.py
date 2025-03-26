class Solution:
    def partitionLabels(self, string: str):
        start = {}
        end = {}

        for i, s in enumerate(string):
            if s not in start:
                start[s] = i
                end[s] = i

            else:
                end[s] = i

        res = []
        pat_start, pat_end = -1, -1
        
        for key in start:
            if pat_end < start[key]:
                # new partition
                width = pat_end - pat_start + 1
                res.append(width)

                pat_start = start[key]
                pat_end = end[key]

            # if this character completely lies in current partition
            elif pat_start <= start[key] and end[key] <= pat_end:
                continue

            # partially lies in range
            else:
                pat_end = end[key]

        width = pat_end - pat_start + 1
        res.append(width)

        return res[1:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
    print(sol.partitionLabels("eccbbbbdec"))
