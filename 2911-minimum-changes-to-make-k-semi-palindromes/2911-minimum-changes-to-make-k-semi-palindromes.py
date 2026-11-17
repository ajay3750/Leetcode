
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[float('inf')] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0
                        groups = length // d

                        for r in range(d):
                            for t in range(groups // 2):
                                a = i + r + t * d
                                b = i + r + (groups - 1 - t) * d

                                if s[a] != s[b]:
                                    changes += 1

                        cost[i][j] = min(cost[i][j], changes)

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for end in range(2 * p, n + 1):
                for start in range(2 * (p - 1), end - 1):
                    dp[p][end] = min(
                        dp[p][end],
                        dp[p - 1][start] + cost[start][end - 1]
                    )

        return dp[k][n]
