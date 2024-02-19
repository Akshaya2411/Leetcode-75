class Solution:
    def reverseVowels(self, s: str) -> str:
        a=""
        if(s == " "):
            res=" "
        else:
            for i in s:
                if(i in "aeiouAEIOU"):
                    a+=i
            a=a[::-1]
            res=""
            m=0
            for i in s:
                if(i in "aeiouAEIOU"):
                    res=res+a[m]
                    m=m+1
                else:
                    res=res+i
           
        return res
            
                

        
