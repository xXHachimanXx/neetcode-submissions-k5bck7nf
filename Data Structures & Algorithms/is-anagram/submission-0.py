class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar - crarace
        #       i     j

        # jar - jam
        # i     j

        if not len(s) == len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for ch in s:
            if count_s.get(ch, 0) != count_t.get(ch, 0):
                return False

        return True
            
            




