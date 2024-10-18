def dfs(graph, start, goal):
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

