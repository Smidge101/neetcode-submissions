class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}

        count = 0
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        for i in s:
            hash_map1[i]= hash_map1.get(i, 0) + 1
        

        for j in t:
            hash_map2[j] = hash_map2.get(j, 0) + 1


        return hash_map1 == hash_map2
        