import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        ans = []
        current_time = 0
        
        for j, task_time in enumerate(tasks):
            current_time = max(current_time, j)
            
            if not free_servers:
                current_time = busy_servers[0][0]
                
            while busy_servers and busy_servers[0][0] <= current_time:
                _, w, i = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (w, i))
                
            w, i = heapq.heappop(free_servers)
            ans.append(i)
            heapq.heappush(busy_servers, (current_time + task_time, w, i))
            
        return ans