class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        for x in nums:
            for i in range(31):
                if (x >> i) & 1:
                    bit_counts[i] += 1
        
        ans = 0
        for _ in range(k):
            curr = 0
            for i in range(31):
                if bit_counts[i] > 0:
                    curr |= (1 << i)
                    bit_counts[i] -= 1
            ans = (ans + curr * curr) % MOD
            
        return ans