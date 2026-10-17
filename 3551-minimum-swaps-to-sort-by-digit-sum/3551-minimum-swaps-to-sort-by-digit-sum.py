class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(val: int) -> int:
            return sum(int(digit) for digit in str(val))

        n = len(nums)
        indexed_nums = [(nums[i], i) for i in range(n)]
        indexed_nums.sort(key=lambda item: (get_digit_sum(item[0]), item[0]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or indexed_nums[i][1] == i:
                continue
                
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][1]
                cycle_size += 1
                
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps