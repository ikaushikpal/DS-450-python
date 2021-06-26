def maxMeetings(start, finish):
    if len(start) == 0:
        return 0
    
    meetings = [(finish[i], start[i]) for i in range(len(start))]
    meetings.sort(key=lambda x: x[0])

    prevStartTime = meetings[0][1]
    prevFinishTime = meetings[0][0]
    counter = 1

    for i in range(1, len(meetings)):
        if meetings[i][1] > prevFinishTime:
            prevStartTime = meetings[i][1]
            prevFinishTime = meetings[i][0]
            counter += 1
    
    return counter


s = [1,3,0,5,8,5]
f = [2,4,6,7,9,9]

print(maxMeetings(s, f))

s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
f = [112960, 114515, 81825, 93424, 54316,35533, 73383, 160252]

print(maxMeetings(s, f))
