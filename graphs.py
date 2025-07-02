class Graphs:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_string = ""

        for node, neighbours in self.adj_list.items():
            graph_string += f"{node} -> {neighbours}\n"

        return graph_string


    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()

        else:
            raise ValueError("Node already exists")


    def add_edge(self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)

        else:
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))


    def bfs(self, start_node):
        visited = set()

        queue = [start_node]
        order = []

        while queue:
            node = queue.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbors(node)

                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]

                    if neighbour not in visited:
                        queue.append(neighbour)

        return order

    def dfs(self, start_node):
        visited = set()

        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbors(node)

                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]

                    if neighbour not in visited:
                        stack.append(neighbour)

        return order


    def obtain_neighbors(self, node):
        return self.adj_list.get(node, set())

    def dijkstra(self, start_node):
        MAX = 999999  # Large number to simulate infinity
        distances = {node: MAX for node in self.adj_list}
        distances[start_node] = 0

        visited = set()

        while len(visited) < len(self.adj_list):
            # Pick the unvisited node with the smallest distance
            min_node = None
            min_distance = MAX

            for node in self.adj_list:
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node

            if min_node is None:
                break  # All remaining nodes are inaccessible

            for neighbor_info in self.adj_list[min_node]:
                if isinstance(neighbor_info, tuple):
                    neighbor, weight = neighbor_info
                else:
                    neighbor = neighbor_info
                    weight = 1  # Default weight for unweighted edges

                if neighbor not in visited:
                    new_distance = distances[min_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

            visited.add(min_node)

        return distances


if __name__ == '__main__':
    graph_obj = Graphs(directed=True)

    graph_obj.add_edge("A", "B", 2)
    graph_obj.add_edge("A", "J", 2)
    graph_obj.add_edge("A", "C", 3)
    # graph_obj.add_edge("A", "D", 4)
    graph_obj.add_edge("B", "D", 4)
    graph_obj.add_edge("D", "C", 7)

    print(graph_obj)

    print("BREADTH FIRST SEARCH:")
    print(graph_obj.bfs("A"))

    print("DEPTH FIRST SEARCH:")
    print(graph_obj.dfs("A"))

    print("DIJKSTRA (Shortest distances from A):")
    shortest = graph_obj.dijkstra("A")
    for node, dist in sorted(shortest.items()):
        print(f"{node}: {dist}")

