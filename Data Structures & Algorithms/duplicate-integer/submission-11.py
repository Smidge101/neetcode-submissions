class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force:
        arr = set()

        for i in nums:
            if i in arr:
                return True

            arr.add(i)

        return False
        