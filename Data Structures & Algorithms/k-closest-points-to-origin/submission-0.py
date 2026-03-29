from math import sqrt

class Point:
    def __init__(self, point, dist):
        self.dist = dist
        self.point = point

class Solution:

    def calculate_distance_to_oririn(self, point):
        x, y = point[0], point[1]
        distance = sqrt(x**2 + y**2)
        return Point(point, distance)

    def heappop(self, heap):
        root = heap[1]
        last = heap.pop()

        if len(heap) > 1:
            heap[1] = last
            self.heapify(1, heap)

        return root

    def heapify(self, i, heap):
        n = len(heap)-1
        left = 2*i
        right = 2*i + 1
        largest = i

        if left <= n and heap[left].dist < heap[i].dist:
            largest = left
        
        if right <= n and heap[right].dist < heap[i].dist:
            largest = right

        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            self.heapify(largest, heap)
        
    def build_max_heap(self, heap):
        n = len(heap)-1

        for i in range(n//2, 0, -1):
            self.heapify(i, heap)
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closests = [] 
        heap = [None] # list of tuples like (distance, [x,y])

        for point in points:
            heap.append(self.calculate_distance_to_oririn(point))
        
        self.build_max_heap(heap)

        for i in range(k):
            k_closests.append(self.heappop(heap).point)
        
        print(k_closests)
        
        return k_closests
        