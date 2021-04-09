from sys import maxsize


class Solution:
    def maxSubArraySum(self, arr, size):
        meh = 0
        msf = -maxsize

        for val in arr:
            meh += val

            if meh < val:
                meh = val

            if msf < meh:
                msf = meh

        return msf
