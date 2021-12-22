import current as current

from common.solver import solver
from pathlib import Path


def load_from_input(test_input=False):
    base_path = Path(__file__).parent
    file = f"{base_path}/test_input.txt" if test_input else f"{base_path}/part1.txt"
    with open(file) as f:
        for line in f:
            for num in line.split(","):
                yield int(num)


@solver
def part1(test_input=False):
    input = list(load_from_input(test_input))
    print(f"{input=}")
    max_val = max(input)
    min_val = min(input)
    print(f"{min_val} :: {max_val}")
    x_pos = min_val
    sum_steps = 99999999

    for pos in range(min_val, max_val+1):
        steps = [abs(pos-x) for x in input]
        # print(f"move to pos: {pos} - {steps}")
        current_sum_steps = sum(steps)
        if current_sum_steps < sum_steps:
            sum_steps = current_sum_steps
            x_pos = pos

    print(f"finding minimun at pos: {x_pos}, sum_steps: {sum_steps}")
    return sum_steps


@solver
def part2(test_input=False):
    pass



if __name__ == '__main__':
    assert part1(True) == 37
    assert part1(False) == "part1"
    assert part2(True) == "part2 - test"
    assert part2(False) == "part2"