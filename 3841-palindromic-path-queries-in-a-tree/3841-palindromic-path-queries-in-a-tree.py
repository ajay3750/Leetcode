class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        import sys
        sys.setrecursionlimit(200000)

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        par, dep, sz, heavy = [-1]*n, [0]*n, [1]*n, [-1]*n

        def dfs(u, p):
            mx = 0
            for v in g[u]:
                if v == p:
                    continue
                par[v], dep[v] = u, dep[u] + 1
                dfs(v, u)
                sz[u] += sz[v]
                if sz[v] > mx:
                    mx, heavy[u] = sz[v], v

        dfs(0, -1)
        head, pos = [0]*n, [0]*n
        timer = 0

        def hld(u, h):
            nonlocal timer
            head[u], pos[u] = h, timer
            timer += 1
            if heavy[u] != -1:
                hld(heavy[u], h)
            for v in g[u]:
                if v != par[u] and v != heavy[u]:
                    hld(v, v)

        hld(0, 0)

        size = 1
        while size < n:
            size *= 2
        seg = [0] * (2 * size)

        for u in range(n):
            seg[size + pos[u]] = 1 << (ord(s[u]) - 97)
        for i in range(size - 1, 0, -1):
            seg[i] = seg[2*i] ^ seg[2*i+1]

        def update(u, c):
            i = size + pos[u]
            seg[i] = 1 << (ord(c) - 97)
            while i > 1:
                i //= 2
                seg[i] = seg[2*i] ^ seg[2*i+1]

        def query(l, r):
            res = 0
            l, r = l + size, r + size
            while l < r:
                if l & 1:
                    res ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= seg[r]
                l //= 2
                r //= 2
            return res

        def path(u, v):
            res = 0
            while head[u] != head[v]:
                if dep[head[u]] < dep[head[v]]:
                    u, v = v, u
                res ^= query(pos[head[u]], pos[u] + 1)
                u = par[head[u]]
            if dep[u] > dep[v]:
                u, v = v, u
            return res ^ query(pos[u], pos[v] + 1)

        ans = []
        for q in queries:
            t = q.split()
            if t[0] == "update":
                update(int(t[1]), t[2])
            else:
                ans.append(path(int(t[1]), int(t[2])).bit_count() <= 1)

        return ans