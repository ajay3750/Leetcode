class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        res = [0] * len(queries)
        cnt = defaultdict(int)
        active_servers = 0
        left = 0
        right = 0
        
        for idx, q in sorted_queries:
            while right < len(logs) and logs[right][1] <= q:
                server_id = logs[right][0]
                if cnt[server_id] == 0:
                    active_servers += 1
                cnt[server_id] += 1
                right += 1
                
            while left < len(logs) and logs[left][1] < q - x:
                server_id = logs[left][0]
                cnt[server_id] -= 1
                if cnt[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            res[idx] = n - active_servers
            
        return res