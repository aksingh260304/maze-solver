# Maze Solver using A* Search

## 📌 Overview

This project implements a **Maze Solver using the A* (A-Star) Search Algorithm** in Python. The program finds the shortest path from a start position to a goal position in a maze while avoiding obstacles. It also provides both console-based and graphical visualization of the search process and the final path.

The A* algorithm is widely used in Artificial Intelligence, robotics, navigation systems, and game development due to its efficiency and optimal pathfinding capabilities.

---

## 🚀 Features

* User-defined maze input
* Shortest path calculation using A* Search
* Manhattan Distance heuristic
* Detection of unreachable goals
* Console visualization of:

  * Start node (S)
  * Goal node (G)
  * Walls (#)
  * Visited nodes (o)
  * Final path (*)
* Graphical visualization using Matplotlib
* Efficient priority queue implementation using `heapq`

---

## 🛠️ Technologies Used

* Python 3
* Heap Queue (`heapq`)
* NumPy
* Matplotlib

---

## 📂 Project Structure

```text
Maze-Solver-AStar/
│
├── maze.py
├── README.md
└── requirements.txt
```

---

## 📖 How A* Search Works

The A* Search Algorithm evaluates nodes using:

```text
f(n) = g(n) + h(n)
```

Where:

* `g(n)` = Cost from the start node to the current node
* `h(n)` = Estimated cost from the current node to the goal node (heuristic)
* `f(n)` = Total estimated cost

This project uses the **Manhattan Distance** heuristic:

```text
h(n) = |x1 - x2| + |y1 - y2|
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Maze-Solver-AStar.git
cd Maze-Solver-AStar
```

### Install Dependencies

```bash
pip install numpy matplotlib
```

---

## ▶️ Running the Project

```bash
python maze.py
```

---

## 📝 Sample Input

```text
Enter number of rows: 5
Enter number of columns: 5

Row 1: 0 0 0 1 0
Row 2: 1 1 0 1 0
Row 3: 0 0 0 0 0
Row 4: 0 1 1 1 0
Row 5: 0 0 0 0 0

Start Row: 0
Start Column: 0

Goal Row: 4
Goal Column: 4
```

---

## 📊 Sample Console Output

```text
S * * # .
# # * # .
o o * * *
. # # # *
. . . . G
```

### Legend

| Symbol | Meaning       |
| ------ | ------------- |
| S      | Start Node    |
| G      | Goal Node     |
| *      | Shortest Path |
| o      | Visited Node  |
| #      | Wall          |
| .      | Empty Cell    |

---

## 🎯 Applications

* GPS Navigation Systems
* Robotics Path Planning
* Video Game AI
* Autonomous Vehicles
* Network Routing

---

## 📚 Learning Outcomes

Through this project, you will learn:

* Graph Search Algorithms
* A* Search Implementation
* Heuristic Functions
* Priority Queues
* Pathfinding Techniques
* Data Visualization in Python

---

## 🔮 Future Improvements

* Diagonal movement support
* Multiple heuristic options
* Animated search visualization
* GUI-based interface using Tkinter or PyQt
* Maze generation functionality

---

## 👨‍💻 Author

**Ankit Kumar**

BCA Student | Python Developer | AI & Software Enthusiast

GitHub: https://github.com/aksingh260304

LinkedIn: https://www.linkedin.com/in/ankit-kumar-479815394/

---

## 📄 License

This project is open-source and available under the MIT License.
