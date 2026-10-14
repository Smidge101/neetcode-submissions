class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if same length
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        hash_map1 = {}
        hash_map2 = {}

    
        for i in range(len_s):
            hash_map1[s[i]] = hash_map1.get(s[i], 0) + 1
            hash_map2[t[i]] = hash_map2.get(t[i], 0) + 1

        return hash_map1 == hash_map2

        