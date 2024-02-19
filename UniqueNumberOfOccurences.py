class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=list(set(arr))
        count=[]
        for i in a:
            count.append(arr.count(i))
        return len(count)==len(list(set(count)))
           
