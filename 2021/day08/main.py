import current as current

from common.solver import solver
from pathlib import Path


def load_from_input(test_input=False):
    base_path = Path(__file__).parent
    file = f"{base_path}/test_input.txt" if test_input else f"{base_path}/part1.txt"
    with open(file) as f:
        for line in f.read().splitlines():
            yield line.split(" | ")



@solver
def part1(test_input=False):
    input_lines = list(load_from_input(test_input))
    occurences = 0
    for input_line in input_lines:
        signal_input, output = input_line
        # print(f"{signal_input} -||- {output}")

        signals = signal_input.split(" ")

        seven_segments = []
        for sig in signals:
            if len(sig) in [2,4,3,7]: # 1,4,7,8
                seven_segments.append(''.join(sorted(sig)))
        # print(f"{seven_segments=}")

        output_vals = output.split(" ")
        for o_val in output_vals:
            occurences += 1 if ''.join(sorted(o_val)) in seven_segments else 0
        #print(f"{occurences=}")
    return occurences


@solver
def part2(test_input=False):
    pass



if __name__ == '__main__':
    assert part1(True) == 26
    assert part1(False) == 0
    assert part2(True) == 0
    assert part2(False) == 0