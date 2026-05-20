from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for q in intervals:
            if result == []:
                result.append(q)
            if result[-1][1] >= q[0]:
                result[-1][1] = max(result[-1][1],q[1])
            else:
                result.append(q)
        return result
