# 743. Network Delay Time

'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
'''

Basic idea: Dijkstra



class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = self.build_graph(times)
        # graph = {node: [(child, dist), (child, dist)]}
        
        hqueue = [(0, K)]
        mindist = {} # save finalized (minimum dist) nodes here
        
        while hqueue:
            d, node = heapq.heappop(hqueue)
            if node in mindist:
                continue            
            mindist[node] = d
            
            for v, w in graph[node]:
                if v in mindist:
                    continue
                heapq.heappush(hqueue, (d+w, v))
                
        res = max(mindist.values())
        return res if len(mindist) == N else -1
    
    def build_graph(self, times):
        graph = collections .defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        return graph