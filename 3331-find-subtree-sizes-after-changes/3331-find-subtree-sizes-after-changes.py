class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        new_parent = list(parent)
        last_seen = {}
        
        def dfs_reparent(u):
            char = s[u]
            prev = last_seen.get(char, -1)
            if prev != -1:
                new_parent[u] = prev
            last_seen[char] = u
            for v in adj[u]:
                dfs_reparent(v)
            last_seen[char] = prev
            
        dfs_reparent(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        def dfs_size(u):
            for v in new_adj[u]:
                dfs_size(v)
                ans[u] += ans[v]
                
        dfs_size(0)
        return ans