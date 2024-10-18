import heapq

def ucs(graph, start, goal):
    """
    Uniform Cost Search (UCS) algorithm to find the least-cost path from the start node to the goal node.

    This implementation uses a priority queue to explore nodes based on their cumulative cost from the start node.

    Parameters:
    - graph: The graph representation.
    - start: The starting node (city).
    - goal: The goal node (city).

    Returns:
    - A tuple containing:
      - A list representing the path taken from start to goal.
      - A float representing the total cost to reach the goal.
      - An integer representing the total number of nodes visited during the search.
      If no path is found, it returns (None, float('inf'), node_count).
    """
    queue = [(0, [start])]  # Priority queue initialized with the starting node and cost 0
    visited = set()          # Set to keep track of visited nodes
    node_count = 0           # Counter for the number of nodes visited

    while queue:
        cost, path = heapq.heappop(queue)  # Get the node with the least cost
        node = path[-1]                    # The current node is the last node in the path

        if node in visited:
            continue  # Skip if the node has already been visited

        node_count += 1  # Increment the node count

        if node == goal:
            return path, cost, node_count  # Return the path, cost, and node count if goal is reached

        for neighbor, dist in graph.get_neighbors(node):
            new_cost = cost + dist  # Update the cost to reach the neighbor
            new_path = list(path)    # Create a new path including the neighbor
            new_path.append(neighbor) # Append the neighbor to the new path
            heapq.heappush(queue, (new_cost, new_path))  # Push the new path and cost to the priority queue

        visited.add(node)  # Mark the current node as visited

    return None, float('inf'), node_count  # Return if no path is found
