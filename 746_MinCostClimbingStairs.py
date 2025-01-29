from solution_check import ProblemSet
import heapq


def minCostClimbingStairsDijkstra(cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        path = [0] + cost + [0]
        
        graph = {}
        for i in range(len(path) - 1):  # Loop to create edges for all but the last node
            graph[i] = []
            if i + 1 < len(path):
                graph[i].append((i + 1, path[i + 1]))
            if i + 2 < len(path):
                graph[i].append((i + 2, path[i + 2]))
        
        # Dijkstra's Algorithm
        def dijkstra(graph, start, end):
            nodes = set(graph.keys())
            for edges in graph.values():
                for dest, _ in edges:
                    nodes.add(dest)
                    
            pq = []
            distances = {vertex: float('infinity') for vertex in nodes}
            distances[start] = 0
            heapq.heappush(pq, (0,start))
            
            while pq:
                current_distance, current_vertex = heapq.heappop(pq)

                # Stop if we reach the end node
                if current_vertex == end:
                    return distances[current_vertex]

                # Skip if a better path was already found
                if current_distance > distances[current_vertex]:
                    continue

                # Explore neighbours
                for neighbour, weight in graph[current_vertex]:
                    distance = current_distance + weight
                    # If a shorter path is found
                    if distance < distances[neighbour]:
                        distances[neighbour] = distance
                        heapq.heappush(pq, (distance, neighbour))
                    

        # Calculate shortest path to the last node
        return dijkstra(graph, 0, len(path)-1)


def minCostClimbingStairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    cost = cost + [0]
    dp = [0] * len(cost)
    
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2,len(dp)):
        dp[i] = cost[i] + min([dp[i-1],dp[i-2]])
        
    return dp[len(dp)-1]

if __name__ == "__main__":
    testcases = {
        "testcase1": {
            "args": ([10,15,20],),
            "solution": 15
        },
        "testcase2": {
            "args": ([1,100,1,1,1,100,1,1,100,1],),
            "solution": 6
        }
    }
    
    ps = ProblemSet(testcases,minCostClimbingStairs)
    
    ps.check_solution()