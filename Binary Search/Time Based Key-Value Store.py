# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


class KeyMap:
    def __init__(self, time, values):
        self.times = [time]
        self.values = [values]
    
    def append(self, time, value):
        self.times.append(time)
        self.values.append(value)
    
    def search(self, targetTime):
        if len(self.times) == 1:
            if self.times[0] <= targetTime:
                return self.values[0]
            else:
                return ''
        
        low, high = 0, len(self.times)-1
        floorIndex = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.times[mid] == targetTime:
                return self.values[mid]

            elif self.times[mid] > targetTime:
                high = mid - 1

            else:
                floorIndex = mid
                low = mid + 1
        
        if floorIndex == -1:
            return ''
        return self.values[floorIndex]
               

class TimeMap:

    def __init__(self):
        self.keyPair = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyPair:
            self.keyPair[key] = KeyMap(timestamp, value)
        else:
            self.keyPair[key].append(timestamp, value)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keyPair:
            return self.keyPair[key].search(timestamp)
        return ''


if __name__ == '__main__':
    timeMap =TimeMap()
    timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.get("foo", 1)         # return "bar"
    timeMap.get("foo", 3)         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4) # store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.get("foo", 4)         # return "bar2"
    timeMap.get("foo", 5)         # return "bar2"