def shotres_way(start_point, finish_point, size_of_labyrinth, labyrinth):
    queue = [start_point]
    dist_to = {start_point: 0}
    prevex_vertex = {start_point: None}
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue
        if vertex == finish_point:
            return dist_to[vertex]
        visited.add(vertex)
        for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            row, col = vertex[0] + direction[0], vertex[1] + direction[1]
            if (
                0 <= row < size_of_labyrinth[0]
                and 0 <= col < size_of_labyrinth[1]
                and (row, col) not in visited
                and labyrinth[row][col] != 0
            ):
                queue.append((row, col))
                dist_to[(row, col)] = dist_to[vertex] + 1
    return None


def read_input(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        start_str = lines[0].strip()
        finish_str = lines[1].strip()
        size_str = lines[2].strip()
        lab = []
        for line in lines[3:]:
            row = [int(x) for x in line.strip().split(',') if x]
            lab.append(row)
    start = tuple(map(int, start_str.split(',')))
    finish = tuple(map(int, finish_str.split(',')))
    size = tuple(map(int, size_str.split(',')))
    return start, finish, size, lab





def write_output(output_file, result):
    with open(output_file, 'w') as f:
        f.write(str(result))


def main():
    input_file = 'C:/Users/User/Desktop/Lab 5/resources/input.txt'
    output_file = 'C:/Users/User/Desktop/Lab 5/resources/output.txt'
    start, finish, size, lab = read_input(input_file)
    result = shotres_way(start, finish, size, lab)
    write_output(output_file, result)


if __name__ == '__main__':
    main()
