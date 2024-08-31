# Example 1:
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"

class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        self.table[key].append((value, int(timestamp)))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        lst = self.table[key]
        s, e = 0, len(lst) - 1
        if timestamp < lst[s][1]:
            return ""
        # binary search
        while s <= e:
            m = s + (e - s) // 2
            if lst[m][1] == timestamp:
                return lst[m][0]
            elif lst[m][1] > timestamp:
                e = m - 1
            else:
                s = m + 1
        return lst[e][0]


timeMap = TimeMap()
# store the key "foo" and value "bar" along with timestamp = 1.
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))  # return "bar"
# return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2,
# then the only value is at timestamp 1 is "bar".
print(timeMap.get("foo", 3))
# store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))  # return "bar2"
print(timeMap.get("foo", 5))  # return "bar2"
