class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index=0
        for i in range(0,len(nums)):
            if(i==0):
                if(0== sum(nums[i+1:len(nums)])):
                    index=i
                    break
            if(sum(nums[:i])==sum(nums[i+1:])):
                index=i
                break
            if(i==len(nums)-1):
                if(0==sum(nums[0:len(nums)-1])):
                    index=-1
                    break
            else:
                index=-1
        return index
                
        
        
