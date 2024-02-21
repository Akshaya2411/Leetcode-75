from numpy import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(nums)):
            c=nums[:i]+nums[i+1:]
            res.append(prod(c))
        return res
        
