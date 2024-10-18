def dls(graph, start, goal, limit=9):
    stack = [(start, [start], 0, 0)]  # Stack holds (node, path, cumulative_distance, depth)
    visited = set()
    node_count = 0

    while stack:
        node, path, current_distance, depth = stack.pop()

        if node in visited or depth > limit:
            continue

        node_count += 1

        if node == goal:
            return path, current_distance, node_count

        visited.add(node)

        for neighbor, distance in graph.get_neighbors(node):
            stack.append((neighbor, path + [neighbor], current_distance + distance, depth + 1))

    return None, 0, node_count  # If no path is found, return 0 distance and the node count


