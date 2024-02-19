class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=set(nums1)
        nums2=set(nums2)
        for i in list(nums2):
            if i in nums1 and i in nums2:
                nums1.remove(i)
                nums2.remove(i)
        return([list(nums1),list(nums2)])
