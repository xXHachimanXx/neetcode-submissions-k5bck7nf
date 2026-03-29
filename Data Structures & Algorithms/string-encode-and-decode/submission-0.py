class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes, encoded = [], ""

        if not strs:
            return ""

        for s in strs:
            sizes.append(len(s))

        for sz in sizes:
            encoded += str(sz)
            encoded += ','

        encoded += '#'
        for s in strs:
            encoded += s

        return encoded 

    def decode(self, s: str) -> List[str]:
        res, sizes = [], []
        sz = ''
        start = -1

        if not s:
            return []

        for i in range(len(s)):
            if s[i] == '#':
                start = i+1
                break
            elif s[i] == ',':
                sizes.append(int(sz))
                sz = ''
            else:
                sz += s[i]
                

        for sz in sizes:
            res.append(s[start : start+sz])
            start += sz

        return res




















