class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        res=[]
        for i in candies:
            res.append(i+extraCandies>=maxi)
        return res
        
