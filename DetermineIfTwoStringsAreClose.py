class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        else:
          a=[]
          b=[]
          c=list(set(list(word1)))
          d=list(set(list(word2)))
          for i,j in zip(c,d):
            b.append(word2.count(i))
            a.append(word1.count(j))
          if(sorted(a)==sorted(b) and sorted(c)==sorted(d)):
            return True
          else:
            return False
        


        
        
        


        
        
