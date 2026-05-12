class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            sorted_chars = sorted(word)
            key = "".join(sorted_chars)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(word)
        return list(hash_map.values())