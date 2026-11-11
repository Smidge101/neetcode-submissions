class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force:
        arr = []

        for i in range(len(nums)):
            if nums[i] in arr:
                return True

            arr.append(nums[i])

        return False
        