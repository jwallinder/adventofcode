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
        # # print(f"{signal_input} -||- {output}")

        signals = signal_input.split(" ")

        seven_segments = []
        for sig in signals:
            if len(sig) in [2,4,3,7]: # 1,4,7,8
                seven_segments.append(''.join(sorted(sig)))
        # # print(f"{seven_segments=}")

        output_vals = output.split(" ")
        for o_val in output_vals:
            occurences += 1 if ''.join(sorted(o_val)) in seven_segments else 0
        # print(f"{occurences=}")
    return occurences


@solver
def part2(test_input=False):
    input_lines = list(load_from_input(test_input))
    totals = 0
    for input_line in input_lines:
        signal_input, output = input_line
        # # print(f"{signal_input} -||- {output}")

        signals = signal_input.split(" ")

        seven_segments = {}
        num_segments_dict = {}
        signals_to_go = [x for x in signals]
        for sig in signals:
            orig_signal = sig
            sig = "".join(sorted(sig))
            if len(sig) == 2:  # [2,4,3,7]: # 1,4,7,8
                seven_segments[sig] = "1"
                num_segments_dict[1] = sig
                signals_to_go.remove(orig_signal)
            if len(sig) == 4:  # [2,4,3,7]: # 1,4,7,8
                seven_segments[sig] = "4"
                num_segments_dict[4] = sig
                signals_to_go.remove(orig_signal)
            if len(sig) == 3:  # [2,4,3,7]: # 1,4,7,8
                seven_segments[sig] = "7"
                num_segments_dict[7] = sig
                signals_to_go.remove(orig_signal)
            if len(sig) == 7:  # [2,4,3,7]: # 1,4,7,8
                seven_segments[sig] = "8"
                num_segments_dict[8] = sig
                signals_to_go.remove(orig_signal)



        # print(f"{signals_to_go=}")
        signals = [x for x in signals_to_go]
        for sig in signals:
            orig_signal = sig
            sig = "".join(sorted(sig))
            if len(sig) == 6: #0,9,6
                if not all(e in sig for e in num_segments_dict[1]):
                    seven_segments[sig] = "6"
                    num_segments_dict[6] = sig
                    signals_to_go.remove(orig_signal)
                elif all(e in sig for e in (set(list(num_segments_dict[4]))|set(list(num_segments_dict[7])))):
                    seven_segments[sig] = "9"
                    num_segments_dict[9] = sig
                    signals_to_go.remove(orig_signal)
                else:
                    seven_segments[sig] = "0"
                    num_segments_dict[0] = sig
                    signals_to_go.remove(orig_signal)
            if len(sig) == 5:
                if all(e in sig for e in num_segments_dict[1]):
                    seven_segments[sig] = "3"
                    num_segments_dict[3] = sig
                    signals_to_go.remove(orig_signal)
                elif all(e in sig for e in set(list(num_segments_dict[4]))-set(list(num_segments_dict[7]))):
                    seven_segments[sig] = "5"
                    num_segments_dict[5] = sig
                    signals_to_go.remove(orig_signal)
                else:
                    seven_segments[sig] = "2"
                    num_segments_dict[2] = sig
                    signals_to_go.remove(orig_signal)


        # print(f"{signals_to_go=}")
        # print(f"{num_segments_dict=}")
        # print(f"{seven_segments=}")

        output_vals = output.split(" ")
        numbers = ""
        for o_val in output_vals:
            key =  ''.join(sorted(o_val))
            numbers += seven_segments[key]
        # print(f"{numbers=}")
        totals += int(numbers)
    return totals



if __name__ == '__main__':
    assert part1(True) == 26
    assert part1(False) == 554
    assert part2(True) == 61229
    assert part2(False) == 990964