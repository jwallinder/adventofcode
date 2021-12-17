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
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2 or y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                # print(f"{x1=}, {y1=}, {x2=}, {y2=}")
                for y in range(min(y1,y2), max(y1,y2)+1):
                    matrix[(x,y)] += 1
                    # print(f"{matrix=}") 

    return sum([1 for value in matrix.values() if value > 1]) 

@solver.solver
def part2(test_input=False):
    pass

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
    assert part1(False) in [5, 8111]
    assert part2(False) in [0, 0]
