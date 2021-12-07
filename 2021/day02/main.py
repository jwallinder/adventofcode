from common.solver import solver


@solver
def part1(test_input=False):

    file = "test_input.txt" if test_input else "part1.txt"

    with open(file) as f:
        lines = f.read().splitlines()
        # print(lines)

    vertical = 0
    horizontal = 0

    for line in lines:
        vert, horiz = process_line(line)
        vertical += vert
        horizontal += horiz

    return vertical * horizontal


def process_line(line):
    direction, movement = lines = line.split(" ")
    movement = int(movement)
    # print(f"{direction=}")
    # print(f"{movement=}")

    if direction == "forward":
        return 0, movement
    if direction == "down":
        return movement, 0
    if direction == "up":
        return -movement, 0


@solver
def part2(test_input=False):

    file = "test_input.txt" if test_input else "part1.txt"

    with open(file) as f:
        lines = f.read().splitlines()
        # print(lines)

    forward = 0
    depth = 0
    aim = 0

    for line in lines:
        aim_delta, forward_delta = process_line(line)
        # print("-------------")
        # print(f"{aim_delta=}, {forward_delta=}")

        forward += forward_delta
        aim += aim_delta
        depth += aim*forward_delta
        # print(f"{forward=}, {aim=}, {depth=}")
    return forward * depth

if __name__ == '__main__':
    part1()
    part2()