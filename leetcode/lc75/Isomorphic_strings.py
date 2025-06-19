class Solution:
    def isIsomorphic(self, s, t):
        map = {}
        for index in range(len(s)):
            if s[index] not in map.keys():
                if t[index] not in map.values():
                    map[s[index]] = t[index]
                else:
                    return False
            else:
                if map[s[index]] != t[index]:
                    return False
        return True

s = Solution()
print(s.isIsomorphic("egg","add"))
print(s.isIsomorphic("egg","adt"))
print(s.isIsomorphic("paper","title"))
print(s.isIsomorphic("egg","adt"))
print(s.isIsomorphic("badc","baba"))
print(s.isIsomorphic("b","a"))