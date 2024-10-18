def heuristic(city, goal):
    """
    Estimate the straight-line distance from a given city to the goal city.

    This heuristic is used in search algorithms to prioritize nodes based on their estimated cost
    to reach the goal. It uses pre-defined straight-line distances to the goal city.

    Parameters:
    - city: The current city for which the heuristic is being calculated.
    - goal: The goal city (not used in this heuristic, but included for consistency with algorithm signatures).

    Returns:
    - An integer representing the estimated straight-line distance from the current city to the goal city.
      If the city is not found in the predefined distances, it returns 0.
    """
    straight_line_distances = {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Dobreta": 242,
        "Eforie": 161,
        "Fagaras": 178,
        "Giurgiu": 77,
        "Hirsova": 151,
        "Iasi": 226,
        "Lugoj": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 98,
        "Rimnicu Vilcea": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374
    }
    return straight_line_distances.get(city, 0)
