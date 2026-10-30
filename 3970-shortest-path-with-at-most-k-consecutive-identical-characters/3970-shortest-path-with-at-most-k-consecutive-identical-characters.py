from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
        pq = [(0, 0, labels[0], 1)]
        dist = {(0, labels[0], 1): 0}

        while pq:
            d, u, last_char, count = heapq.heappop(pq)

            if d != dist.get((u, last_char, count), float('inf')):
                continue

            if u == n - 1:
                return d

            for v, w in graph[u]:
                if labels[v] == last_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                state = (v, labels[v], new_count)
                new_dist = d + w

                if new_dist < dist.get(state, float('inf')):
                    dist[state] = new_dist
                    heapq.heappush(
                        pq,
                        (new_dist, v, labels[v], new_count)
                    )

        return -1