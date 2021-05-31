class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def is_list(self):
        for idx in range(self.row):
            if len(self.graph[idx]) != self.row:
                return True
        return False

    def list_to_matrix(self):
        matrix = []
        for idx in range(self.row):
            row = [0] * self.row
            for edge in self.graph[idx]:
                row[edge[0]] = edge[1]
            matrix.append(row)
        return matrix

    def bfs(self, s, t, parent):
        visited = [False] * self.row

        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for idx, val in enumerate(self.graph[u]):
                if visited[idx] is False and val > 0:
                    queue.append(idx)
                    visited[idx] = True
                    parent[idx] = u
        return True if visited[t] else False

    def FordFulkerson(self, source, sink):
        parent = [-1] * self.row

        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
