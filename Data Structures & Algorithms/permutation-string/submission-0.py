class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tmp = ''
        s1 = sorted(s1)

        for c in s2:
            tmp = tmp + c
            if len(tmp) == len(s1):
                if sorted(tmp) == s1:
                    return True
                
                tmp = tmp[1:]
        
        return False


