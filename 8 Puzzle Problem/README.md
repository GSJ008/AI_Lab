# **8-Puzzle Solver: BFS, DFS, and Heuristic Search**

## **Problem Statement**
The **8-Puzzle Problem** is a sliding puzzle consisting of a 3×3 grid with 8 numbered tiles (`1–8`) and one empty space (`0`).  
The objective is to slide the tiles into the empty space to reach the **goal state**:

Goal State:
1 2 3
4 5 6
7 8 0

Given an **initial configuration**, the program determines whether the puzzle can be solved using:
- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Heuristic Search** (Greedy Best-First Search with misplaced tiles heuristic)

---

## **Objectives**
1. Implement **DFS**, **BFS**, and **Heuristic Search** for solving the 8-puzzle.
2. Understand **state space search** in AI.
3. Compare the algorithms in terms of:
   - Time complexity
   - Space complexity
   - Solution path length

---

## **State Representation**
- **`vector<vector<int>>`** (C++ STL) represents the 3×3 puzzle.
- The empty tile (`0`) can be moved **up, down, left, or right** if within bounds.
- States are encoded into a **string** for storage in a `set` to track visited configurations.

---

## **Algorithms**

### **1. Depth-First Search (DFS)**
- Explores as far as possible along a branch before backtracking.
- Uses a **stack**.
- May get stuck in deep branches; not guaranteed to find the shortest solution.
- **Memory Usage:** Low.

**Pseudocode:**
```text
Push initial state to stack
While stack not empty:
    Pop top state
    If state is goal:
        Success
    Generate all possible moves
    Push unvisited states to stack
If stack empty:
    No solution

```
---

### **2. Breadth-First Search (BFS)**
- Explores all nodes at the current depth before moving deeper.
- Uses a **queue**.
- **Guarantees the shortest solution** if one exists.
- **Memory Usage:** High.

**Pseudocode:**
```text
Enqueue initial state
While queue not empty:
    Dequeue front state
    If state is goal:
        Success
    Generate all possible moves
    Enqueue unvisited states
If queue empty:
    No solution

```
---

### **3. Heuristic Search (Greedy Best-First Search)**
- Uses a **priority queue** to explore states closer to the goal first.
- The code uses the **misplaced tiles heuristic**:
  

**Pseudocode:**
```text
Insert initial state into priority queue with priority = misplaced tiles
While priority queue not empty:
    Remove state with smallest priority
    If state is goal:
        Success
    Generate all possible moves
    For each move:
        Calculate misplaced tiles
        Insert into priority queue with that priority
If priority queue empty:
    No solution
```

**Advantages:**
- Faster than BFS for large state spaces.
- Goal-directed search.
- Memory usage often lower than BFS.

**Limitations:**
- Not guaranteed to find the shortest path.
- Heuristic choice affects performance.

---

## **Move Generation**
From a given state:
1. Find the location of the empty tile (`0`).
2. Generate up to 4 possible moves:
   - **Up**    → swap with tile above.
   - **Down**  → swap with tile below.
   - **Left**  → swap with tile to the left.
   - **Right** → swap with tile to the right.

---

## **Data Structures Used**
| Purpose                   | Data Structure |
|---------------------------|---------------|
| Puzzle grid               | `vector<vector<int>>` |
| DFS frontier              | `stack`       |
| BFS frontier              | `queue`       |
| Heuristic search frontier | `priority_queue` |
| Visited states tracking   | `set<string>` |
| Parent mapping (optional) | `map<string, string>` |

---

## **Complexity Analysis**
Let:
- **b** = branching factor (≤ 4 for 8-puzzle)
- **d** = depth of solution
- **N** = number of states in search space (≤ 9! = 362,880 for 8-puzzle)

| Algorithm         | Time Complexity | Space Complexity | Notes |
|-------------------|-----------------|------------------|-------|
| DFS               | O(b^d)          | O(b·d)           | May explore deep, irrelevant paths. |
| BFS               | O(b^d)          | O(b^d)           | Finds shortest path but high memory usage. |
| Heuristic Search  | O(b·log b × d) to O(b^d) | O(b^d) | Performance depends heavily on heuristic quality. |

---

## **Comparison Table**
| Feature             | DFS        | BFS        | Heuristic Search (GBFS) |
|---------------------|-----------|-----------|--------------------------|
| Completeness        | No        | Yes       | Yes (with good heuristic)|
| Optimality          | No        | Yes       | No                       |
| Memory Usage        | Low       | High      | Moderate                 |
| Time Complexity     | O(b^d)    | O(b^d)    | O(b·log b × d) to O(b^d) |
| Search Direction    | Blind     | Blind     | Goal-directed            |
---

## **Sample Outputs**

### **DFS**
```text
Input State:
1 2 3
4 5 6
8 0 7

Output:
Goal reached!
```

### **BFS**
```text
Input State:
8 1 2
0 4 3
7 6 5

Output:
Goal reached!
```

### **Heuristic Search**
```text
Initial state:
1 2 3
4 0 6
7 5 8

h=2
1 2 3
4 0 6
7 5 8
h=1
1 2 3
4 5 6
7 0 8
h=0
1 2 3
4 5 6
7 8 0
Goal reached!

```
---

## **How to Run**
1. Compile and run the required file:
```bash
# DFS
g++ 8puzzle.cpp -o dfs
./dfs

# BFS
g++ 8puzzleBFS.cpp -o bfs
./bfs

# Heuristic Search
g++ heuristic.cpp -o heuristic
./heuristic
