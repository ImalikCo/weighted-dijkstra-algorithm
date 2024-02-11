import collections
import heapq

def shortestPath(edges, source, sink):
    graph = collections.defaultdict(list)
    for left, right, minutes in edges:
        graph[left].append((minutes,right))

    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == sink:
                return (cost, path)
            for minutes, neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+minutes, neighbour, path))
    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "C", 10),
        ("B", "D", 5),
        ("C", "E", 5),
        ("E", "F", 10),
        ("D", "F", 11),
        ("D", "G", 11),
        ("F", "H", 7),
        ("G", "H", 12),
    ]

    print ("The shortest path is: ", shortestPath(edges, "A", "H"))
