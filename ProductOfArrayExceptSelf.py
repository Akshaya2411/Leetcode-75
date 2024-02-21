from numpy import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        m=prod(nums)
        for i in range(0,len(nums)):
            if(nums[i]==0):
                c=nums[:i]+nums[i+1:]
                res.append(prod(c))
            else:
                res.append(m//nums[i])
        return res
        
