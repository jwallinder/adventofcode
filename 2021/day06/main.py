from common import solver
from pathlib import Path
from collections import defaultdict

@solver.solver
def part1(test_input=False):
    input= list(load_from_input(test_input))


    lanternfish = input
    for day in range(1,81):

        sum_new_fishes = len(list(filter(lambda x: x == 0, lanternfish)))

        lanternfish = [fish-1 if fish >0 else 6 for fish in lanternfish]
        lanternfish.extend([8]*sum_new_fishes)
        #print(f"{day=}: {lanternfish}")

    return len(lanternfish)

@solver.solver
def part2(test_input=False):
    pass



def load_from_input(test_input=False):
    base_path = Path(__file__).parent
    file = f"{base_path}/test_input.txt" if test_input else f"{base_path}/part1.txt"
    with open(file) as f:
        for line in f:
            for num in line.split(","):
                yield int(num)


if __name__ == '__main__':
    assert part1(False) in [5934, 365131]
    assert part2(False) in ["WRONG", "WRONG"]
