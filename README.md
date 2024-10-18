# 🚗 Automatic path finder using AI algorithms

This project implements several search algorithms for finding the optimal path between cities in a graph-based road network. The project is inspired by the famous "Arad to Bucharest" pathfinding problem and includes both uninformed and informed search strategies, such as **A\*** and **Greedy search**, with custom heuristic functions.

## 🗺️ Features

- **Graph Representation**: Cities are modeled as nodes, and roads between them as edges with distances.
- **Six Pathfinding Algorithms**: Implementations of BFS, DFS, UCS, DLS, A*, and Greedy search.
- **Heuristic Support**: Custom heuristic for A* and Greedy algorithms based on straight-line distances.
- **Execution Time Measurement**: Each algorithm's execution time is measured for performance evaluation.

## 🚀 Algorithms

- **BFS**: Breadth-First Search
- **DFS**: Depth-First Search
- **UCS**: Uniform Cost Search
- **DLS**: Depth-Limited Search (with a depth limit of 3)
- **A\***: A* Search using a heuristic function
- **Greedy Search**: Heuristic-driven pathfinding

## 🧠 Heuristic Function

The heuristic function is based on straight-line distances between cities, guiding the informed search algorithms (A\* and Greedy search). You can experiment with different heuristic approaches to see their impact on performance.

## 🛠️ How It Works

The program models a graph of cities connected by roads and uses the following algorithms to search for the optimal route:

1. **Breadth-First Search (BFS)**: Explores all nodes at the current depth before moving to the next depth level.
2. **Depth-First Search (DFS)**: Recursively explores deeper paths first, backtracking when no further paths exist.
3. **Uniform Cost Search (UCS)**: Always expands the least costly node, ensuring the optimal path is found.
4. **Depth-Limited Search (DLS)**: DFS with a depth limit to prevent deep recursive paths.
5. **A\* Search**: Uses both path cost and heuristic to find the most efficient path.
6. **Greedy Search**: Prioritizes nodes that appear closest to the goal, though it may not always find the optimal path.

## 📊 Example of City Map

```plaintext
Arad -- 75 --> Zerind
Zerind -- 71 --> Oradea
Oradea -- 151 --> Sibiu
```

In this case, the program attempts to find the optimal path from **Arad** to **Bucharest**, using various search algorithms.

## 📂 Code Structure

- `auto-path-finder.py`: The main entry point for running the search algorithms.
- `graph.py`: Defines the graph structure (cities and roads).
- `a_star.py`: Implements the A* algorithm.
- `bfs.py`: Implements the Breadth-First Search algorithm.
- `dfs.py`: Implements the Depth-First Search algorithm.
- `dls.py`: Implements the Depth-Limited Search algorithm.
- `ucs.py`: Implements the Uniform Cost Search algorithm.
- `greedy.py`: Implements the Greedy Search algorithm.
- `heuristic.py`: Defines the heuristic function used by A* and Greedy Search.

## 🏃‍♂️ Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/L000Pz/Auto-path-finder
   cd Auto-path-finder
   ```
2. Run the project:

   ```bash
   python auto-path-finder.py
   ```
3. You have to manually enter:

- **Starting city**: The city where the search starts.
- **Destination city**: The goal city to reach.

4. The program will print the results for each algorithm, including:

- **Path**: The sequence of cities from start to goal.
- **Cost/Count**: The total distance or the number of nodes explored.
- **Time**: Time taken to execute the algorithm.

### Example output:
```plaintext
BFS: Path: ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'], Cost: 450, Time: 0.0012 seconds
DFS: Path: ['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta', 'Craiova', 'Pitesti', 'Bucharest'], Time: 0.0009 seconds
...
```
## 🔍 Performance Evaluation
The program evaluates the following performance metrics for each algorithm:

- **Path Cost**: Total distance from the starting city to the destination.
- **Execution Time**: Each algorithm's time to find a solution.
- **Nodes Explored**: The number of cities visited during the search.


## 💡 Contribution
Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or new features.
