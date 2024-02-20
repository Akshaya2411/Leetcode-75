class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res=0
        for i in range(0,len(flowerbed)):
            if((i==len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i]==0) or (i==0 and flowerbed[i]==0 and flowerbed[i+1]==0)):
                res=res+1
                flowerbed[i] = 1
            else:
                if(flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                    res=res+1
                    flowerbed[i] = 1
        print(res)
        return (n<=res)
        
