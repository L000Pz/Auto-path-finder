import heapq

def a_star(graph, start, goal, heuristic):
    """
    Performs the A* algorithm to find the shortest path from start to goal in a weighted graph.

    Parameters:
    - graph: An object representing the graph, which must have a method `get_neighbors(node)` 
      that returns a list of tuples (neighbor, distance).
    - start: The starting node in the graph.
    - goal: The target node in the graph.
    - heuristic: A function that estimates the cost from a given node to the goal. It should 
      accept two parameters: the current node and the goal node, and return a non-negative number.

    Returns:
    - path: A list of nodes representing the path from start to goal, or None if no path exists.
    - g_cost: The total cost from start to goal, or float('inf') if no path exists.
    - node_count: The number of nodes explored during the search.
    """
    queue = [(0, [start])]  # Priority queue initialized with the start node
    visited = set()          # Set to keep track of visited nodes
    g_costs = {start: 0}    # Dictionary to store the cost of reaching each node
    node_count = 0           # Count of nodes explored

    while queue:
        f_cost, path = heapq.heappop(queue)  # Get the node with the lowest f_cost
        node = path[-1]                      # Current node is the last in the path

        if node in visited:
            continue  # Skip if already visited

        node_count += 1  # Increment the explored node count

        if node == goal:
            return path, g_costs[node], node_count  # Return path and costs if goal is reached

        for neighbor, dist in graph.get_neighbors(node):
            g_cost = g_costs[node] + dist  # Cost to reach neighbor
            h_cost = heuristic(neighbor, goal)  # Heuristic cost to goal
            f_cost = g_cost + h_cost  # Total cost

            # Update costs and add neighbor to queue if it's a better path
            if neighbor not in g_costs or g_cost < g_costs[neighbor]:
                g_costs[neighbor] = g_cost
                heapq.heappush(queue, (f_cost, path + [neighbor]))

        visited.add(node)  # Mark the node as visited

    return None, float('inf'), node_count  # Return if no path exists
