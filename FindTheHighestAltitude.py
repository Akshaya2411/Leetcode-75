class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        for i,j in zip(gain,a):
            a.append(i+j)
        return(max(a))
