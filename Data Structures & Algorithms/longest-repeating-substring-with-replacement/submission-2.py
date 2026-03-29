class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = left = res = 0

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            maxf = max(maxf, count[c])

            # window_size - maxf > k
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res
        