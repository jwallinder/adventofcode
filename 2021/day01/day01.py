from input import part1_input as input
from time import perf_counter_ns




def solver(fn):
    def wrap(*args, **kwargs):
        start = perf_counter_ns()
        res = fn(*args, **kwargs)
        elapsed_time = perf_counter_ns() - start
        print(f"{fn.__name__}:")
        print(f"Answer is: {res}")
        print(f"Took: {elapsed_time / NS_TO_MICRO} µs\n")

    return wrap


@solver
def part1():
    # print(input)
    lines = input.splitlines()
    prev = int(lines[0])
    increased = 0

    for line in lines[1:]:
        line = int(line)
        # print(f"comparing {prev=}, {line=}")
        if line > prev:
            increased += 1
            # print(f"{increased=}")
        prev = line
    return increased


@solver
def part2():
    lines = input.splitlines()
    lines = [int(i) for i in lines]
    prev = sum(lines[0:3])
    print(lines[0:3])
    print(sum(lines[0:3]))
    increased = 0
    for offset, _ in enumerate(lines):
        # print(offset)
        if (offset +3 > len(lines)):
            break
        current = sum(lines[offset: offset + 3])
        if current > prev:
            increased += 1
        prev = current
    return increased


if __name__ == '__main__':
    part1()
    part2()
