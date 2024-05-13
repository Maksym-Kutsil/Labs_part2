from collections import defaultdict


def max_flow(input_file):
    maximum_flow = 0
    try:
        farms, stores, roads = read_data_from_file(input_file)
        roads = [[vertex[0], vertex[1], int(vertex[2])] for vertex in roads]
        if not roads or len(farms) == 0 or len(stores) == 0:
            return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    for farm in farms:
        roads.append(["F", farm, float('inf')])
    for store in stores:
        roads.append([store, "S", float('inf')])

    graph = defaultdict(dict[int])

    for road in roads:
        start_vertex, end_vertex, weight = road
        graph[start_vertex][end_vertex] = weight
    graph = dict(graph)

    while True:
        path = dfs(graph)
        if not path:
            break
        maximum_flow += decrease_weight_on_path(graph, path)

    return maximum_flow


def decrease_weight_on_path(graph, path):
    min_weight = float('inf')
    for i in range(len(path) - 1):
        start_vertex = path[i]
        end_vertex = path[i + 1]
        min_weight = min(graph[start_vertex][end_vertex], min_weight)

    for i in range(len(path) - 1):
        start_vertex = path[i]
        end_vertex = path[i + 1]
        if graph[start_vertex][end_vertex] == min_weight:
            del graph[start_vertex][end_vertex]
        else:
            graph[start_vertex][end_vertex] -= min_weight

    return min_weight


def dfs(graph):
    if not graph:
        return None
    queue = ['F']
    previous_vertex = {
        'F': None,
    }
    visited = set()

    while queue:
        vertex = queue.pop()
        if vertex in visited:
            continue

        if vertex == 'S':
            return get_path(previous_vertex, vertex, 'F')

        visited.add(vertex)
        for neighbour in graph[vertex]:
            queue.append(neighbour)
            previous_vertex[neighbour] = vertex

    return None


def get_path(from_dict, last_vertex, start_vertex):
    path = []
    while last_vertex != start_vertex:
        path.append(last_vertex)
        last_vertex = from_dict[last_vertex]
    path.append(start_vertex)
    return path[::-1]


def read_data_from_file(file_name):
    with open(f"C:\\Labs_part2\\resourses\\{file_name}", "r") as file:
        roads = file.readlines()
        start_vertexes = roads[0].strip().split()
        destination_vertexes = roads[1].strip().split()
        edges = [line.strip().split() for line in roads[2:]]
    return start_vertexes, destination_vertexes, edges