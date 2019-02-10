cmake_minimum_required(VERSION 3.13)


project(Hailey)

set(CMAKE_CXX_STANDARD 14)

add_executable(Hailey src/all.h src/algorithms/Graph/Kruskal.cpp src/algorithms/Graph/GraphBuilder.h src/algorithms/Graph/BFS.cpp src/algorithms/Graph/DFS.cpp src/algorithms/Graph/Prim.cpp src/algorithms/Graph/DisjointSet.cpp src/algorithms/Graph/Dijikstra.cpp src/algorithms/Graph/Astar.cpp src/algorithms/Graph/Cycle.cpp src/algorithms/Graph/TopologicaLSorting.cpp src/algorithms/Graph/BellmanFord.cpp src/algorithms/Graph/FloydWarshal.cpp src/algorithms/Graph/SCC.cpp src/algorithms/Graph/2SAT.cpp src/algorithms/Graph/3SAT.cpp)