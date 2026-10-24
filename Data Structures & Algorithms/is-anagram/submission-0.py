class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = sorted(s.lower())
        t_list = sorted(t.lower())

        if s_list == t_list:
            return True
        else:
            return False
        