from collections import deque

def bfs(graph, start, goal):
    """
    Breadth-First Search (BFS) algorithm to find the shortest path from the start node to the goal node.

    This implementation uses a queue to explore all neighbors at the present depth prior to moving on to nodes 
    at the next depth level.

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
    visited = set()                   # Set to keep track of visited nodes
    queue = deque([[(start, 0)]])     # Queue initialized with the starting node and distance
    node_count = 0                    # Counter for the number of nodes visited

    while queue:
        path = queue.popleft()        # Get the first path from the queue
        node, current_distance = path[-1]  # Unpack the last node and its current distance

        if node in visited:
            continue  # Skip if the node has already been visited

        node_count += 1  # Increment the node count

        for neighbor, distance in graph.get_neighbors(node):
            new_path = list(path)  # Create a new path including the neighbor
            new_path.append((neighbor, current_distance + distance))  # Add neighbor with updated distance
            queue.append(new_path)  # Add new path to the queue

            if neighbor == goal:
                final_path = [n for n, _ in new_path]  # Extract only the nodes from the path
                total_distance = current_distance + distance  # Final total distance
                return final_path, total_distance, node_count  # Return the path, distance, and node count

        visited.add(node)  # Mark the current node as visited

    return None, 0, node_count  # If no path is found, return 0 distance
