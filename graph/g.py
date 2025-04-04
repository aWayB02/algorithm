from collections import defaultdict, deque


class Graph:

    def __init__(self, e):
        self.e = e
        self.edges = defaultdict(list)

        for v1, v2 in e:
            self.edges[v1].append(v2)
            self.edges[v2].append(v1)

    def bfs_shortest_path(self, start, end):
        """Находит кратчайший путь от вершины start до вершины end"""
        # Очередь для хранения пути
        queue = deque([(start, [start])])  # (текущая вершина, путь до неё)

        # Множество посещённых вершин
        visited = set()
        visited.add(start)

        while queue:
            current_node, path = queue.popleft()

            # Если мы нашли конечную вершину, возвращаем путь
            if current_node == end:
                return path

            # Добавляем соседей в очередь
            for neighbor in self.edges[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None  # Если путь не найден


edges = [(1, 5), (1, 4), (1, 2), (2, 3), (2, 5), (5, 6), (6, 3), (6, 4)]
graph = Graph(edges)

# Ищем кратчайший путь от 1 до 3
start = 1
end = 9
path = graph.bfs_shortest_path(start, end)
print(f"Кратчайший путь от {start} до {end}: {path}")
