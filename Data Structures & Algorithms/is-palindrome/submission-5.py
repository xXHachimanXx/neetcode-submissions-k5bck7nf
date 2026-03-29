class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(s)
        new_string = ''
        for ch in s:
            if ch.isalnum():
                new_string += ch.lower()

        l, r = 0, len(new_string)-1
        for i in range(len(new_string)):
            if r == l:
                break
            if new_string[r] != new_string[l]:
                return False

            l += 1
            r -= 1

        return True

        
        
        