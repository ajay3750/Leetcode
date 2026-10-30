from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        ans = 0
        remaining = k

        for d in diff:
            if d > left:
                remaining -= d - left
                ans += left * left
            else:
                ans += d * d

        ans -= remaining * (2 * left - 1)

        return ans