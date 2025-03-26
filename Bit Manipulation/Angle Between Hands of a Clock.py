# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

# Answers within 10-5 of the actual value will be accepted as correct.

 

# Example 1:
# Input: hour = 12, minutes = 30
# Output: 165


# Example 2:
# Input: hour = 3, minutes = 30
# Output: 75


# Example 3:
# Input: hour = 3, minutes = 15
# Output: 7.5

# NOTE:
## Hour Hand
# In 12 hours Hour hand complete whole circle and cover 360°
# So, 1 hour = 360° / 12 = 30°

# Since 1 hours = 30°
# In 1 minute, hours hand rotate -> 30° / 60 = 0.5°
# So total angle because of minutes by hour hand is minutes/60 * 30 or minutes * 0.5

## Minute Hand
# In 60 minutes Minute Hand completes whole circle and cover 360°.
# So, 1 minute -> 360° / 60 = 6°


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minPos = minutes * 6
        hourPos = (hour%12 * 30) + (minutes / 2)
        angle = abs(hourPos - minPos)
        return min(angle, 360 - angle)
# Time Complexity: O(1)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.angleClock(12, 30))
    print(sol.angleClock(3, 30))
    print(sol.angleClock(3, 15))