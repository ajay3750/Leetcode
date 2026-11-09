import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        busy = []
        count = [0] * k

        tree = [0] + [i & -i for i in range(1, k + 1)]

        def update(i, val):
            i += 1
            while i <= k:
                tree[i] = tree[i]+val
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s = s+ tree[i]
                i -= i & -i
            return s

        def find(target):
            idx = 0
            bit = 1 << (k.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= k and tree[nxt] < target:
                    idx = nxt
                    target -= tree[nxt]
                bit >>= 1

            return idx

        for i in range(len(arrival)):
            t = arrival[i]

            while busy and busy[0][0] <= t:
                end, server = heapq.heappop(busy)
                update(server, 1)

            total = query(k)
            if total == 0:
                continue

            start = i % k
            before = query(start)

            if total > before:
                server = find(before + 1)
            else:
                server = find(1)

            update(server, -1)
            count[server] += 1

            heapq.heappush(busy, (t + load[i], server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]