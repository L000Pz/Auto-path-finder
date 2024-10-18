from a_star import a_star
from bfs import bfs
from dfs import dfs
from dls import dls
from heuristic import heuristic
from ucs import ucs
from greedy import greedy_search

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, city1, city2, distance):
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
        self.graph[city1].append((city2, distance))
        self.graph[city2].append((city1, distance))

    def get_neighbors(self, city):
        return self.graph[city] if city in self.graph else []

import time

def measure_algorithm(algorithm, graph, start, goal, heuristic=None):
    start_time = time.time()

    if algorithm.__name__ == 'a_star' and heuristic:
        result = algorithm(graph, start, goal, heuristic)
    else:
        result = algorithm(graph, start, goal)

    time_taken = time.time() - start_time
    return result, time_taken





# Construct the graph with the cities and distances
graph = Graph()

# Adding edges with distances between cities
graph.add_edge("Arad", "Zerind", 75)
graph.add_edge("Zerind", "Oradea", 71)
graph.add_edge("Oradea", "Sibiu", 151)
graph.add_edge("Arad", "Sibiu", 140)
graph.add_edge("Arad", "Timisoara", 118)
graph.add_edge("Timisoara", "Lugoj", 111)
graph.add_edge("Lugoj", "Mehadia", 70)
graph.add_edge("Mehadia", "Dobreta", 75)
graph.add_edge("Dobreta", "Craiova", 120)
graph.add_edge("Craiova", "Rimnicu Vilcea", 146)
graph.add_edge("Craiova", "Pitesti", 138)
graph.add_edge("Rimnicu Vilcea", "Sibiu", 80)
graph.add_edge("Rimnicu Vilcea", "Pitesti", 97)
graph.add_edge("Pitesti", "Bucharest", 101)
graph.add_edge("Fagaras", "Sibiu", 99)
graph.add_edge("Fagaras", "Bucharest", 211)
graph.add_edge("Bucharest", "Giurgiu", 90)
graph.add_edge("Bucharest", "Urziceni", 85)
graph.add_edge("Urziceni", "Hirsova", 98)
graph.add_edge("Hirsova", "Eforie", 86)
graph.add_edge("Urziceni", "Vaslui", 142)
graph.add_edge("Vaslui", "Iasi", 92)
graph.add_edge("Iasi", "Neamt", 87)




# پارامترهای ورودی
start_city = "Arad"
goal_city = "Bucharest"

# اجرای الگوریتم‌ها و گزارش نتایج
algorithms = [bfs, dfs, ucs, dls, a_star, greedy_search]
for algorithm in algorithms:
    if algorithm == dls:
        result, time_taken = measure_algorithm(algorithm, graph, start_city, goal_city, 3)  # محدودیت عمق در DLS
    elif algorithm in [a_star, greedy_search]:
        result, time_taken = measure_algorithm(algorithm, graph, start_city, goal_city, heuristic)
    else:
        result, time_taken = measure_algorithm(algorithm, graph, start_city, goal_city)
    
    if result:
        if isinstance(result, tuple):
            path, cost_or_count = result[0], result[1]
            print(f"{algorithm.__name__.upper()}: Path: {path}, Cost/Count: {cost_or_count}, Time: {time_taken:.4f} seconds")
        else:
            print(f"{algorithm.__name__.upper()}: Path: {result}, Time: {time_taken:.4f} seconds")
    else:
        print(f"{algorithm.__name__.upper()}: No path found.")







