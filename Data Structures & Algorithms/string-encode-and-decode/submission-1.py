class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            length = len(s)
            res.append(str(length) + "#" + s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            right_end = j + length + 1
            res.append(s[j + 1: right_end])
            i  = right_end

        return res