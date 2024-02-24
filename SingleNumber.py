class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=list(set(nums))
        for i in a:
            if(nums.count(i)==1):
                return i
                break
        
