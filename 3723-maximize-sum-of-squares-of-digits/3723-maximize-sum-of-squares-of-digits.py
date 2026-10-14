class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        nines = sum // 9
        remainder = sum % 9
        
        if remainder > 0:
            return "9" * nines + str(remainder) + "0" * (num - nines - 1)
        
        return "9" * nines + "0" * (num - nines)