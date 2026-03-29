import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = deque()
        count = Counter(tasks)
        max_heap = [-c for c in count.values()]

        heapq.heapify(max_heap)

        while max_heap or queue:
            time += 1

            if max_heap:
                c = 1 + heapq.heappop(max_heap)
                if c != 0:
                    queue.append([c, time+n])

            if queue and queue[0][1] == time:
                el = queue.popleft()
                heapq.heappush(max_heap, el[0])

        return time
        