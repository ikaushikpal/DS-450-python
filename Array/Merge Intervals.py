class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = []
        pat_start, pat_end = intervals[0][0],  intervals[0][1]
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if pat_end < start:
                # new partition
                res.append([pat_start, pat_end])

                pat_start = start
                pat_end = end

            # if this character completely lies in current partition
            elif pat_start <= start and end <= pat_end:
                continue

            # partially lies in range
            else:
                pat_end = end

        res.append([pat_start, pat_end])

        return res