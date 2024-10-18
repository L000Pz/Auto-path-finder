import heapq

import heapq

def greedy_search(graph, start, goal, heuristic):
    """
    Greedy search algorithm to find the path from start to goal based on heuristic.

    Parameters:
    - graph: The graph representation.
    - start: The starting node (city).
    - goal: The goal node (city).
    - heuristic: The heuristic function to estimate the cost to the goal.

    Returns:
    - A tuple containing the path taken and the total distance (cost) to reach the goal.
    """
    queue = [(0, [start])]  # (estimated cost, path)
    visited = set()
    total_distance = {start: 0}  # Track total distance to each node
    node_count = 0

    while queue:
        _, path = heapq.heappop(queue)
        node = path[-1]

        if node in visited:
            continue

        node_count += 1

        if node == goal:
            return path, total_distance[node]  # Return path and total distance to the goal

        for neighbor, dist in graph.get_neighbors(node):
            if neighbor not in total_distance or total_distance[node] + dist < total_distance[neighbor]:
                total_distance[neighbor] = total_distance[node] + dist  # Update total distance to neighbor
                h_cost = heuristic(neighbor, goal)
                heapq.heappush(queue, (h_cost, path + [neighbor]))

        visited.add(node)

    return None, node_count  # Return None and node count if no path is found

