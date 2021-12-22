from common import solver
from pathlib import Path
from collections import defaultdict

@solver.solver
def part1(test_input=False):
    input= list(load_from_input(test_input))


    return lemon(input, 80)

@solver.solver
def part2(test_input=False):
    input = list(load_from_input(test_input))

    return lemon(input, 256)


def lemon(input, days):
    lanternfish = input

    fish_dict = defaultdict(lambda : 0)
    fish_dict[0] = 0
    fish_dict[1] = 0
    fish_dict[2] = 0
    fish_dict[3] = 0
    fish_dict[4] = 0
    fish_dict[5] = 0
    fish_dict[6] = 0
    fish_dict[7] = 0
    fish_dict[8] = 0

    for f in input:
        fish_dict[f] += 1

    #print(f"{fish_dict}")

    for day in range(1,days+1):
        new_fishes = fish_dict.get(0,0)
        fish_dict = {key-1: value for key, value in fish_dict.items()}
        del fish_dict[-1]

        if fish_dict.get(6) or new_fishes:
            fish_dict[6] = fish_dict.get(6,0) +new_fishes

        fish_dict[8] = new_fishes
        # print(f"{day=}: {fish_dict=}")

        #print(f"{day=}: {lanternfish}")
    fish_vals = fish_dict.values()
    #print(f"{fish_vals=}")
    # print(f"{sum(fish_vals)=}")
    return sum(fish_vals)


def load_from_input(test_input=False):
    base_path = Path(__file__).parent
    file = f"{base_path}/test_input.txt" if test_input else f"{base_path}/part1.txt"
    with open(file) as f:
        for line in f:
            for num in line.split(","):
                yield int(num)


if __name__ == '__main__':
    assert part1(True) == 5934
    assert part1(False) == 365131
    assert part2(True) == 26984457539
    assert part2(False) == "WRONG"
