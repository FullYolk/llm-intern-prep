import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        pri_que = []
        for i in counts:
            heapq.heappush(pri_que,(counts[i],i))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        res = [item[1] for item in pri_que]
        return res