class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res=0
        if s == "":
            return True
        else:
            for i in s:
                if i in t:
                    res+=1
                    t=t[t.index(i)+1:]
            print(res)   
            if res==len(s):
                return True
            else:
                return False
                




        
