from common.solver import solver


@solver
def part1(test_input=False):
    file = "test_input.txt" if test_input else "part1.txt"
    with open(file) as f:
        lines = f.read().splitlines()

    running_sum = [0] * len(lines[0])
    # print(sum)
    for line in lines:
        current = [int(x) for x in line]
        # print (f"{current=}")
        running_sum = [sum(x) for x in zip(running_sum, current)]


    # print(f"{running_sum=}")

    gamma = [1 if x> len(lines)/2 else 0 for x in running_sum]
    # print(f"  {gamma=}")
    epsilon = [0 if x else 1 for x in gamma]
    # print(f"{epsilon=}")

    gamma = int("".join(str(x) for x in gamma),2)
    epsilon = int("".join(str(x) for x in epsilon),2)
    # print(f"  {gamma=}")
    # print(f"{epsilon=}")

    return gamma * epsilon


@solver
def part2(test_input=False):
    pass


if __name__ == '__main__':
    assert part1(True) in [1307354, 198]
    assert part2(False) in [230]
