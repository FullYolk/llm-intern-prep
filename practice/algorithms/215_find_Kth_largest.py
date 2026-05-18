import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hea = []
        for i in nums:
            heapq.heappush(hea,i)
            if len(hea) > k:
                heapq.heappop(hea)
        return hea[0]