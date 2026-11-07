class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num)) # O(log k), k times
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num)) # O(log k), upto (n-k) times
        top = [num for freq, num in heap] # O(k)
        return top