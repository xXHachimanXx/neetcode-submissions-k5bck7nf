class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        # [1,2,2,3,3,3,3]
        # {1: 1, 2: 2, 3: 4}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        res = []
        for i in range(k):
            m = None
            max_num = None
            for num in dic:
                if m is None or dic[num] > m:
                    m = dic[num]
                    max_num = num

            if max_num is not None:
                res.append(max_num)

            dic.pop(max_num)

        return res

        
        
        