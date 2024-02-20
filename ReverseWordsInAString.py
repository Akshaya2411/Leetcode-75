class Solution:
    def reverseWords(self, s: str) -> str:
        a= s.split()[::-1]
        a=" ".join(a)
        return a
