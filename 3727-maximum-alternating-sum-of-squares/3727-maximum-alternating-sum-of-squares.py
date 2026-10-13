class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs, reverse=True)

        n = len(nums)
        k = (n + 1) // 2

        ans = sum(x * x for x in nums[:k]) - sum(x * x for x in nums[k:])

        return ans