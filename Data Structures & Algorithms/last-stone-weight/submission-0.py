
class Solution:
    def heapify(self, heap, parent):
        
        n = len(heap)-1
        largest = parent
        left, right = 2*parent, 2*parent+1

        if left <= n and heap[left] > heap[largest]:
            largest = left
        if right <= n and heap[right] > heap[largest]:
            largest = right
        
        if largest != parent:
            heap[largest], heap[parent] = heap[parent], heap[largest]
            self.heapify(heap, largest)

    def heappush(self, heap, val):
        heap.append(val)

        def heappush_aux(heap, i):
            parent = i//2

            if i > 1 and heap[i] > heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                heappush_aux(heap, parent)

        heappush_aux(heap, len(heap)-1)

    def heappop(self, heap):

        root = heap[1]
        last = heap.pop()

        if len(heap) > 1:
            heap[1] = last
            self.heapify(heap, 1)

        return root
    
    def build_max_heap(self, heap):
        n = len(heap) - 1
        for i in range(n // 2, 0, -1):
            self.heapify(heap, i)

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.insert(0, None)
        
        self.build_max_heap(stones)
        
        while len(stones) > 2:
            s1 = self.heappop(stones)
            s2 = self.heappop(stones)

            print(stones)

            if s1 != s2:
                self.heappush(stones, s1 - s2)
            print(stones)

        stones.append(0)
        return stones[1]
            

        