Depth First Search

Good Learning Materials:

Tutorial by Reducible:
https://www.youtube.com/watch?v=PMMc4VsIacU

Graph Traversal
Given a graph, we start at a single vertex and finding an way to visit every other vertex of the graph

We have many graph traversal algorithms eg:
- pre order traversal
- post order traversal

DFS Applications:
Connected Components
Path Finding
Topological Sort
Strongly Connected Components
Shortest Path
Maze Generation
Maze Solving

 
Depth First Search is a graph traversal algorithm that explores as far as possible along each branch before backtracking.

Back Tracking
Backtracking is a technique for solving problems by trying to build a solution incrementally and removing those solutions that fail to satisfy the constraints of the problem.

Backtracking is a form of depth-first search, and is used extensively in constraint satisfaction problems, such as the classic 8-queens puzzle and the more complex knight's tour.

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Backtracking can be viewed as a special case of divide-and-conquer, and a systematic way of trying different solution attempts (the candidates). In contrast, divide-and-conquer is when we divide the problem into subproblems, solve the subproblems, and then combine the solutions to the subproblems to get the solution to the original problem.

Backtracking is different from dynamic programming in that backtracking builds candidates incrementally, and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Depth First Search
In depth first search the order of traversal is left to right.

You can explore graphs as you like unless their is a constraint that you need to follow.

Topological Sort
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

For example, a topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. For example, another topological sorting of the following graph is “4 5 2 3 0 1”. The first vertex in topological sorting is always a vertex with in-degree as 0 (source vertex).

Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs. In computer science, applications of this type arise in instruction scheduling, ordering of formula cell evaluation when recomputing formula values in spreadsheets, logic synthesis, determining the order of compilation tasks to perform in makefiles, data serialization, and resolving symbol dependencies in linkers