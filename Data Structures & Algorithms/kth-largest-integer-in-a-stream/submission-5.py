class KthLargest:

    def heappop(self, nums):
        smaller = nums[0]
        nums[0], nums[-1] = nums[-1], nums[0]
        nums.pop()

        self.heapify(nums, len(nums), 0)

        return smaller
    
    def heappush(self, nums, val):
        nums.append(val)
        i = len(nums) - 1
        n = len(nums)

        while i > 0:
            parent = (i-1)//2
            if nums[i] < nums[parent]:
                nums[i], nums[parent] = nums[parent], nums[i]
                i = parent
            else:
                break

    def heapify(self, nums, n, parent):
        smaller = parent
        left = 2*parent + 1
        right = 2*parent + 2

        if left < n and nums[left] < nums[smaller]:
            smaller = left
        if right < n and nums[right] < nums[smaller]:
            smaller = right
        
        if smaller != parent:
            nums[parent], nums[smaller] = nums[smaller], nums[parent]
            self.heapify(nums, n, smaller)

    def build_min_heap(self, nums):
        n = len(nums)

        # heapify from the first node with childrens (bottom-top)
        for i in range((n//2)-1, -1, -1):
            self.heapify(nums, n, i)
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.build_min_heap(nums)
        self.minHeap = nums
        
        while len(self.minHeap) > k:
            self.heappop(self.minHeap)

    def add(self, val: int) -> int:
        self.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            self.heappop(self.minHeap)
        
        return self.minHeap[0]
        
        

        
