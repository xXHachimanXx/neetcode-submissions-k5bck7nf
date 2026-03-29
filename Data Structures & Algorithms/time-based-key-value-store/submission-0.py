class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []

        self.timeMap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        values = self.timeMap[key]
        res = ""
        for val, tmstmp in values:
            if tmstmp <= timestamp:
                res = val

        return res
        
