class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar        carrace
        # {r:2, a:2, c:2, e: 1}
        # {r:2, a:2, c:2, e: 1}

        if s == t:
            return True
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}

        for ch in s:
            if ch not in dict_s:
                dict_s[ch] = 0
            dict_s[ch] += 1
        for ch in t:
            if ch not in dict_t:
                dict_t[ch] = 0
            dict_t[ch] += 1
        
        for key in dict_s:

            if key not in dict_t or dict_t[key] != dict_s[key]:
                return False

        return True

        



        