from input import part1_input as input


def part1():
    print(input)
    lines = input.splitlines()
    prev = int(lines[0])
    increased= 0

    for line in lines[1:]:
        line = int(line)
        print(f"comparing {prev=}, {line=}")
        if line > prev:
            increased += 1
            print(f"{increased=}")
        prev = line
    return increased


if __name__ == '__main__':
    print(part1())
