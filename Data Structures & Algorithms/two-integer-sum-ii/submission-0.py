class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr, right_ptr = 0, len(numbers) - 1

        while left_ptr < right_ptr:
            curSum = numbers[left_ptr] + numbers[right_ptr]
            if curSum > target:
                right_ptr -= 1
            elif curSum < target:
                left_ptr += 1

            else:
                return [left_ptr + 1, right_ptr + 1]
        return
        