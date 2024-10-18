def dls(graph, start, goal, limit=9):
    """
    Depth-Limited Search (DLS) algorithm to find a path from the start node to the goal node 
    within a specified depth limit.

    This implementation uses a stack for backtracking and limits the depth of the search 
    to prevent exploring too deep.

    Parameters:
    - graph: The graph representation.
    - start: The starting node (city).
    - goal: The goal node (city).
    - limit: The maximum depth to explore. Default is 9.

    Returns:
    - A tuple containing:
      - A list representing the path taken from start to goal.
      - An integer representing the total distance (cost) to reach the goal.
      - An integer representing the total number of nodes visited during the search.
      If no path is found, it returns (None, 0, node_count).
    """
    stack = [(start, [start], 0, 0)]  # Stack holds (node, path, cumulative_distance, depth)
    visited = set()                    # Set to keep track of visited nodes
    node_count = 0                     # Counter for the number of nodes visited

    while stack:
        node, path, current_distance, depth = stack.pop()  # Unpack the current node and its details

        if node in visited or depth > limit:
            continue  # Skip if the node has already been visited or if depth exceeds limit

        node_count += 1  # Increment the node count

        if node == goal:
            return path, current_distance, node_count  # Return the path, distance, and node count if goal is reached

        visited.add(node)  # Mark the current node as visited

        for neighbor, distance in graph.get_neighbors(node):
            # Add neighbors to the stack with updated path, distance, and depth
            stack.append((neighbor, path + [neighbor], current_distance + distance, depth + 1))

    return None, 0, node_count  # Return if no path is found
