import heapq

def ucs(graph, start, goal):
    queue = [(0, [start])]
    visited = set()
    node_count = 0

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node in visited:
            continue

        node_count += 1

        if node == goal:
            return path, cost, node_count

        for neighbor, dist in graph.get_neighbors(node):
            new_cost = cost + dist
            new_path = list(path)
            new_path.append(neighbor)
            heapq.heappush(queue, (new_cost, new_path))

        visited.add(node)

    return None, float('inf'), node_count
