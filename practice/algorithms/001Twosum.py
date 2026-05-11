class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums): //Pythonic的遍历方法 i为下标 num为值
            if num in hash_map:
                return [i,hash_map[num]]
            else:
                hash_map[target-num] = i