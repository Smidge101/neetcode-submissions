class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}

        for i in s:
            hash_map1[i] = hash_map1.get(i, 0) + 1

        for j in t:
            hash_map2[j] = hash_map2.get(j, 0) + 1

        return hash_map1 == hash_map2
         
        