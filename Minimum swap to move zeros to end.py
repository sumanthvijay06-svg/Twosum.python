class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        zero_count = nums.count(0)
        target_zero_start = n - zero_count
        left, right = 0, n - 1
        swaps = 0
        
        while left < target_zero_start and right >= target_zero_start:
            while left < target_zero_start and nums[left] != 0:
                left += 1
            while right >= target_zero_start and nums[right] == 0:
                right -= 1
            if left < target_zero_start and right >= target_zero_start:
                nums[left], nums[right] = nums[right], nums[left]
                swaps += 1
                left += 1
                right -= 1
                
        return swaps
