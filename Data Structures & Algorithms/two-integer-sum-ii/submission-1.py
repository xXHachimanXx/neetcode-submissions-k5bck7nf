class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)

        # numbers=[2,3,4]
        # target=6
        # res [1]

        for i in range(n):
            res.append(i+1)
            for j in range(i+1, n):
                if numbers[res[-1]-1] + numbers[j] == target:
                    res.append(j+1)
                    return res
            res.pop()
        
        return []
