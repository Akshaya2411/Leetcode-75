class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_word=""
        for i, j in zip(word1,word2):
            new_word=new_word+i+j
        if(len(word1)<len(word2)):
            new_word+=word2[len(word1):]
        else:
             new_word+=word1[len(word2):]
        return(new_word)
