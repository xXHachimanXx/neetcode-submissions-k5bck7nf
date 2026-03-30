class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = defaultdict(int)
        for num in nums:
            count_map[num] -= 1
        
        heap = []
        for num in count_map:
            count = count_map[num]
            heap.append((count, num))
        
        heapq.heapify(heap)
        result = []

        for _ in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)
        
        return result


        




        

        