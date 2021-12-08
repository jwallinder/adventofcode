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


    print(f"{running_sum=}")

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
    file = "test_input.txt" if test_input else "part1.txt"
    with open(file) as f:
        lines = f.read().splitlines()

    bitcount = len(lines[0])

    oxygen_rating = calculate_oxygen_rating(lines, 0)
    co2_scrubber_rating = calculate_co2_scrubber_rating(lines,0)
    print(f"{oxygen_rating=}")
    print(f"{co2_scrubber_rating=}")

    return oxygen_rating * co2_scrubber_rating


def calculate_co2_scrubber_rating(lines, index):
    zeros = []
    ones = []
    for line in lines:
        if line[index] == '1':
            ones.append(line)
        else:
            zeros.append(line)

    to_ret = zeros if len(zeros) <= len(ones) else ones
    print(f"co2:{to_ret=}")
    if len(lines[0]) == index +1 or len(to_ret) == 1:
        return int(to_ret[0],2)
    else:
        return calculate_co2_scrubber_rating(to_ret, index+1)


def calculate_oxygen_rating(lines, index):
    zeros = []
    ones = []
    for line in lines:
        if line[index] == '1':
            ones.append(line)
        else:
            zeros.append(line)
    to_ret = ones if len(ones) >= len(zeros) else zeros
    # print(f"oxy:{to_ret=}")
    if len(lines[0]) == index +1:
        return int(to_ret[0],2)
    else:
        return calculate_oxygen_rating(to_ret, index+1)


if __name__ == '__main__':
    assert part1(True) in [198, 1307354]
    assert part2(False) in [230, 482500]
