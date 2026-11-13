class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        ops = 0
        q = deque()
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            cnt = 1
            while q and q[0][0] < nums[l]:
                val, c = q.popleft()
                ops += (nums[l] - val) * c
                cnt += c
            q.appendleft((nums[l], cnt))
            
            while ops > k:
                val, c = q.pop()
                ops -= val - nums[r]
                if c > 1:
                    q.append((val, c - 1))
                r -= 1
                
            ans += r - l + 1
            
        return ans