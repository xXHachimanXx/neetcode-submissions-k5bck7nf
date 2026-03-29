import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # [1,4,3,2], h = 9
        # [1,4,3,2] k = 1 -> 10 hours
        # [1,2,2,1] k = 2 -> 6 hours

        # We will test the k's possibilities until h. Else, return -1 or None
        # [25,10,23,4], h = 4 
        # k = 1

        # n = len(piles)

        # if n > h:
        #     return -1
        
        # k, agr = 1, h+1
        # while agr > h:
        #     agr = 0
        #     for pile in piles:
        #         agr +=  math.ceil(pile / k)

        #     k += 1

        # return k-1

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/k)
            
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res
                
                
            

        