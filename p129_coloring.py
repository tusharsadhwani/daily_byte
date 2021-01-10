"""
Given an undirected graph determine whether it is bipartite.

Note: A bipartite graph, also called a bigraph, is a set of graph
vertices decomposed into two disjoint sets such that no two graph
vertices within the same set are adjacent.

Ex: Given the followinig graph...

graph = [[1, 3], [0, 2], [1, 3], [0, 2]]

0----1
|    |
|    |
3----2

return true.

Ex: Given the followinig graph...

graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

0----1
| \  |
|  \ |
3----2

return false.
"""


from typing import List, Set


def is_bipartite(graph: List[List[int]]) -> bool:
    group_a: Set[int] = set()
    group_b: Set[int] = set()

    group = group_a
    other_group = group_b

    for vertex, neighbours in enumerate(graph):
        group.add(vertex)
        for neighbour in neighbours:
            if neighbour in group:
                return False

            other_group.add(neighbour)

        group, other_group = other_group, group

    return True


def main() -> None:
    """Main function"""
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    # graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

    print(is_bipartite(graph))


if __name__ == "__main__":
    main()
