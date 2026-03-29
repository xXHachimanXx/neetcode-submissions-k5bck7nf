class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #      i  j
        # [30,38,30,36,35,40,28]
        # [ 1  0  0  0  0  0  0]

        n   = len(temperatures) 
        res = [0]*n
        

        for i in range(n):
            counter = 1
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = counter
                    break
                elif j+1 == n:
                    res[i] = 0
                else:
                    counter += 1
                    
        return res
                


            