import time
from a_star import a_star
from bfs import bfs
from dfs import dfs
from dls import dls
from heuristic import heuristic
from ucs import ucs
from greedy import greedy_search

class Graph:
    """
    Represents a graph using an adjacency list.

    Attributes:
        graph (dict): A dictionary where the keys are nodes (cities) 
                      and the values are lists of tuples (neighbor, distance).
    """

    def __init__(self):
        self.graph = {}
    
    def add_edge(self, city1, city2, distance):
        """
        Adds an edge between two cities with the given distance.

        Args:
            city1 (str): The first city.
            city2 (str): The second city.
            distance (int): The distance between city1 and city2.
        """
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))

    def get_neighbors(self, city):
        """
        Returns the neighbors of a given city.

        Args:
            city (str): The city for which to get neighbors.

        Returns:
            list: A list of tuples representing the neighboring cities 
                  and their distances.
        """
        return self.graph[city] if city in self.graph else []

def measure_algorithm(algorithm, graph, start, goal, heuristic=None):
    """
    Measures the time taken to execute a pathfinding algorithm.

    Args:
        algorithm (function): The pathfinding algorithm function to be executed.
        graph (Graph): The graph on which to execute the algorithm.
        start (str): The starting city.
        goal (str): The goal city.
        heuristic (function, optional): The heuristic function for A* and Greedy search.

    Returns:
        tuple: A tuple containing the result of the algorithm and the time taken.
    """
    start_time = time.time()

    if algorithm.__name__ == 'a_star' and heuristic:
        result = algorithm(graph, start, goal, heuristic)
    elif algorithm.__name__ == 'greedy_search' and heuristic:
        result = algorithm(graph, start, goal, heuristic)
    else:
        result = algorithm(graph, start, goal)

    time_taken = time.time() - start_time
    return result, time_taken

# Construct the graph with the cities and distances
graph = Graph()

# Adding edges with distances between cities
edges = [
    ("Arad", "Zerind", 75),
    ("Zerind", "Oradea", 71),
    ("Oradea", "Sibiu", 151),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Dobreta", 75),
    ("Dobreta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Craiova", "Pitesti", 138),
    ("Rimnicu Vilcea", "Sibiu", 80),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Pitesti", "Bucharest", 101),
    ("Fagaras", "Sibiu", 99),
    ("Fagaras", "Bucharest", 211),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87),
]

for edge in edges:
    graph.add_edge(*edge)

start_city = "Arad"
goal_city = "Bucharest"

# List of pathfinding algorithms to test
algorithms = [bfs, dfs, ucs, dls, a_star, greedy_search]
for algorithm in algorithms:
    if algorithm == dls:
        result, time_taken = measure_algorithm(algorithm, graph, start_city, goal_city, 3)  # Depth limit for DLS
    elif algorithm in [a_star, greedy_search]:
        result, time_taken = measure_algorithm(algorithm, graph, start_city, goal_city, heuristic)  # Pass heuristic
    else:
        result, time_taken = measure_algorithm(algorithm, graph, start_city, goal_city)
    
    # Output results
    if result:
        if isinstance(result, tuple):
            path, cost_or_count = result[0], result[1]
            print(f"{algorithm.__name__.upper()}: Path: {path}, Cost/Count: {cost_or_count}, Time: {time_taken:.4f} seconds")
        else:
            print(f"{algorithm.__name__.upper()}: Path: {result}, Time: {time_taken:.4f} seconds")
    else:
        print(f"{algorithm.__name__.upper()}: No path found.")