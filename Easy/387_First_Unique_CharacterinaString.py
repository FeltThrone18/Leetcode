def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i,c in enumerate(s):
            if dict[c] == 1:
                return i
        return -1
