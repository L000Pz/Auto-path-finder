def dfs(graph, start, goal):
    """
    Depth-first search (DFS) algorithm to find a path from the start node to the goal node.

    This implementation keeps track of the cumulative distance traveled to reach each node
    and uses a stack for backtracking.

    Parameters:
    - graph: The graph representation.
    - start: The starting node (city).
    - goal: The goal node (city).

    Returns:
    - A tuple containing:
      - A list representing the path taken from start to goal.
      - An integer representing the total distance (cost) to reach the goal.
      - An integer representing the total number of nodes visited during the search.
      If no path is found, it returns (None, 0, node_count).
    """
    stack = [[(start, 0)]]  # Stack now holds tuples (node, cumulative_distance)
    visited = set()
    node_count = 0

    while stack:
        path = stack.pop()
        node, current_distance = path[-1]  # Unpack the last node and its current distance

        if node in visited:
            continue

        node_count += 1

        for neighbor, distance in graph.get_neighbors(node):
            new_path = list(path)
            new_path.append((neighbor, current_distance + distance))  # Add the neighbor with updated distance
            stack.append(new_path)

            if neighbor == goal:
                final_path = [n for n, _ in new_path]  # Extract only the nodes from the path
                total_distance = current_distance + distance  # Final total distance
                return final_path, total_distance, node_count

        visited.add(node)

    return None, 0, node_count  # If no path is found, return 0 distance
