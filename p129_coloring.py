r"""
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
from typing import TypeVar

T = TypeVar('T')


class Group(set[T]):
    """Named Set"""

    def __init__(self, *, name: str) -> None:
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return self.name


def _is_bipartite(
        vertex: int,
        graph: list[list[int]],
        group: set[int],
        other_group: set[int]) -> bool:
    """Recursive definition of is_bipartite"""
    if vertex in other_group:
        return False

    if vertex in group:
        return True

    group.add(vertex)
    print(vertex, 'added to', group)

    neighbours = graph[vertex]
    for neighbour in neighbours:
        if not _is_bipartite(neighbour, graph, group=other_group, other_group=group):
            return False

    return True


def is_bipartite(graph: list[list[int]]) -> bool:
    """Checks if given graph is bipartite or not"""
    group_a: set[int] = Group(name='Red')
    group_b: set[int] = Group(name='Black')

    group = group_a
    other_group = group_b

    vertex = 0
    return _is_bipartite(vertex, graph, group, other_group)


def main() -> None:
    """Main function"""
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    # graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

    print(is_bipartite(graph))


if __name__ == "__main__":
    main()
