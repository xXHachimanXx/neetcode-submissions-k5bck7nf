class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = res = 0
        subs = set()
        n = len(s)

        for right in range(n):
            while s[right] in subs:
                subs.remove(s[left])
                left += 1
            subs.add(s[right])
            res = max(res, right - left+1)
        
        return res