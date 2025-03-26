class MySolution:    
    def minimumPlatform(self, n, arrival, departure):
        if n == 0:
            return 0

        no_of_platforms = 0
        trainsTime = [(arrival[x], departure[x]) for x in range(n)]
        trainsTime.sort(key=lambda x: x[1])

        while len(trainsTime):
            prevArrivalTime = trainsTime[0][0]
            prevDepartureTime = trainsTime[0][1]
            trainsTimeCopy = []

            for i in range(1, len(trainsTime)):
                if trainsTime[i][0] > prevDepartureTime:
                    prevArrivalTime = trainsTime[i][0]
                    prevDepartureTime = trainsTime[i][1]
                else:
                    trainsTimeCopy.append(trainsTime[i])
            
            trainsTime = trainsTimeCopy
            
            no_of_platforms += 1

        return no_of_platforms


class Solution:    
    def minimumPlatform(self, n, arrival, departure):
        if n == 0:
            return 0

        maximum_train_at_time = no_of_platforms = 0

        arrival.sort()
        departure.sort()

        i = j = 0
        
        while i<n and j<n:
            if arrival[i] <= departure[j]:
                i += 1
                maximum_train_at_time += 1
            else:
                j += 1
                maximum_train_at_time -= 1

            no_of_platforms = max(no_of_platforms, maximum_train_at_time)
            
        return no_of_platforms

if __name__ == '__main__':
    sol = Solution()
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = 6

    print(sol.minimumPlatform(n, arr, dep))