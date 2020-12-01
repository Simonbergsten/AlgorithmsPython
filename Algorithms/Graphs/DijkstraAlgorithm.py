from _collections import defaultdict

class Solution:
    def networkDelayTime(self, times, N, K):
        g = defaultdict(list)

        for u,v,cost in times:
            g[u].append((cost, v))

        min_heap = [(0,k)]

        visited = set()
        distance = {i:float("inf") for i in range(1, N+1)}

        distance[k] = 0

        while min_heap:
            cur_dist, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            if len(visited) == N:
                return cur_dist

            for direct_distance, v in g[u]:
                if cur_dist + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_dist + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))

        return -1
    




