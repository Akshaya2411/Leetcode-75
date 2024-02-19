import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd=math.gcd(len(str1),len(str2))
        pattern=str1[:gcd]
        if(str1 == pattern*(len(str1)//gcd) and str2 == pattern*(len(str2)//gcd)):
            return pattern
        else:
            return ""
