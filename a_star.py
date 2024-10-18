import heapq

def a_star(graph, start, goal, heuristic):
    queue = [(0, [start])]
    visited = set()
    g_costs = {start: 0}
    node_count = 0

    while queue:
        f_cost, path = heapq.heappop(queue)
        node = path[-1]

        if node in visited:
            continue

        node_count += 1

        if node == goal:
            return path, g_costs[node], node_count

        for neighbor, dist in graph.get_neighbors(node):
            g_cost = g_costs[node] + dist
            h_cost = heuristic(neighbor, goal)
            f_cost = g_cost + h_cost

            if neighbor not in g_costs or g_cost < g_costs[neighbor]:
                g_costs[neighbor] = g_cost
                heapq.heappush(queue, (f_cost, path + [neighbor]))

        visited.add(node)

    return None, float('inf'), node_count
