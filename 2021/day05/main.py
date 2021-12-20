from common import solver
from pathlib import Path
from collections import defaultdict

@solver.solver
def part1(test_input=False):
    lines = load_from_input(test_input)
    # print(list(lines))
    matrix = defaultdict(int)
    for line in lines:
        # print(f"this is line: {line}")
        p1, p2 = line
        y1, x1 = p1
        y2, x2 = p2

        if x1 == x2 or y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                # print(f"{x1=}, {y1=}, {x2=}, {y2=}")
                for y in range(min(y1,y2), max(y1,y2)+1):
                    matrix[(x,y)] += 1
                    # print(f"{matrix=}") 
    print_matrix(matrix)
    return sum([1 for value in matrix.values() if value > 1]) 

@solver.solver
def part2(test_input=False):
    lines = load_from_input(test_input)
    # print(list(lines))
    matrix = defaultdict(int)
    for line in lines:
        # print(f"this is line: {line}")
        p1, p2 = line
        x1, y1 = p1
        x2, y2 = p2
        # print(f"{p1} -> {p2}")
        val =1
        if x1 == x2 or y1 == y2:
            # print(f"{p1} -> {p2} is straight")
            for x in range(min(x1,x2), max(x1,x2)+1):
                # print(f"{x1=}, {y1=}, {x2=}, {y2=}")
                for y in range(min(y1,y2), max(y1,y2)+1):
                    matrix[(x,y)] += 1
                    # print(f"{matrix=}")
            #print("matrix after straight line")
            #print(f"{matrix=}")
            #print_matrix(matrix)

        if abs(x1-x2) == abs(y1-y2):
            # print(f"{p1} -> {p2} is diagonal")
            x_dir = 1 if x2-x1 >0 else -1
            y_dir = 1 if y2-y1 >0 else -1
            y = y1
            # print(f"{x_dir=}, {y_dir=}, {list(range(x1, x2 + x_dir, x_dir))}")
            for x in range(x1, x2 + x_dir, x_dir):
                    #print(f"before ({x},{y}) = {matrix[(x, y)]}")
                    matrix[(x, y)] +=1

                    # print(f"after ({x},{y}) = {matrix[(x, y)]}")
                    y += y_dir
                    # print(f"{matrix=}")
        # print("matrix after point")
        # print(f"{matrix=}")
        # print_matrix(matrix)
    llist = [value for value in matrix.values() if value > 1]
    # print(f"{len(llist)} elements - {llist}")
    return sum([1 for value in matrix.values() if value > 1])


def print_matrix(matrix):
    print("=start print_matrix ===============================")
    keys_list = matrix.keys()
    x_vals = [k[0] for k in keys_list]
    max_x = max(x_vals)
    # print(f"{x_vals}")
    #print(f"{max_x}")
    y_vals = [k[1] for k in keys_list]
    max_y = max(y_vals)
    # print(f"{y_vals}")
    #print(f"{max_y}")

    for x in range(max_x+1):
        line = ""
        for y in range(max_y+1):
            val = matrix[(x,y)]
            print_val = str(val) if val > 0 else "."
            #print(f"({x},{y}) = {val} => {print_val}")
            line += print_val
        print(line)
    print("================================")

def load_from_input(test_input=False):
    base_path = Path(__file__).parent
    file = f"{base_path}/test_input.txt" if test_input else f"{base_path}/part1.txt"
    with open(file) as f:
        for line in f:
            point = []
            for a in line.split(" -> "):
                x, y = a.split(",")
                point.append((int(x), int(y)))
            yield point


if __name__ == '__main__':
    assert part1(True) in [5, 8111]
    assert part2(False) in [12, 22088]
