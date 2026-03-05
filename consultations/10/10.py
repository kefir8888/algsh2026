class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [float("-inf") for _ in range(k)]

        window = sum(nums[:k])
        result = window
        for i in range(k - 1, len(nums)):
            pt = (i + 1) % k
            prefix[pt] = max(window, window + prefix[pt])
            result = max(result, prefix[pt])
            window -= nums[i - k + 1]
            if i + 1 < len(nums):
                window += nums[i + 1]
        
        return result