import heapq

def greedy_search(graph, start, goal, heuristic):
    queue = [(0, [start])]
    visited = set()
    node_count = 0

    while queue:
        _, path = heapq.heappop(queue)
        node = path[-1]

        if node in visited:
            continue

        node_count += 1

        if node == goal:
            return path, node_count

        for neighbor, _ in graph.get_neighbors(node):
            h_cost = heuristic(neighbor, goal)
            heapq.heappush(queue, (h_cost, path + [neighbor]))

        visited.add(node)

    return None, node_count
