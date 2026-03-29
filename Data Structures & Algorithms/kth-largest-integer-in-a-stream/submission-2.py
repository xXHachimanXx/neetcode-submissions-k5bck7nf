from typing import List

class KthLargest:

    def heappop(self, nums):
        if not nums:
            raise IndexError("heap vazio")

        top = nums[0]
        nums[0], nums[-1] = nums[-1], nums[0]
        nums.pop()
        self.heapify(nums, len(nums), 0)
        return top

    def heappush(self, nums, val):
        nums.append(val)
        i = len(nums) - 1

        # Corrigido: subir o elemento enquanto for menor que o pai
        while i > 0:
            parent = (i - 1) // 2
            if nums[i] < nums[parent]:
                nums[i], nums[parent] = nums[parent], nums[i]
                i = parent
            else:
                break

    def heapify(self, nums, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[left] < nums[smallest]:
            smallest = left
        if right < n and nums[right] < nums[smallest]:
            smallest = right

        if smallest != i:
            nums[i], nums[smallest] = nums[smallest], nums[i]
            self.heapify(nums, n, smallest)

    def build_min_heap(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        self.build_min_heap(self.minHeap)

        # Mantém apenas os k maiores elementos (heap de tamanho k)
        while len(self.minHeap) > k:
            self.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Se o heap ainda não tem k elementos, só insere
        if len(self.minHeap) < self.k:
            self.heappush(self.minHeap, val)
        # Se o novo valor for maior que o menor (minHeap[0]), troca
        elif val > self.minHeap[0]:
            self.heappop(self.minHeap)
            self.heappush(self.minHeap, val)

        # O menor no heap de tamanho k é o k-ésimo maior
        return self.minHeap[0]
