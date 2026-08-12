class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        array_list = []

        for i in range(len(nums)):
            current = target - nums[i]
            
            if current in hash_map:
                array_list.append(hash_map[current])
                array_list.append(i)
            hash_map[nums[i]] = i

        return array_list
        