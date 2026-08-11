class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dupe_hash = {}
        count = 0

        for i in nums:
            if i in dupe_hash:
                return True

            dupe_hash[i] = count
            count += 1

        return False
