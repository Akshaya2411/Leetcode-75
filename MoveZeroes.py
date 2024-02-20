class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=nums.count(0)
        nums[:] = list(filter(lambda x: x!= 0, nums))
        nums += [0] * c
        return nums
      
