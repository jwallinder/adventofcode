from common.solver import solver
import pprint

@solver
def part1(test_input=False):
    file = "test_input.txt" if test_input else "part1.txt"
    with open(file) as f:
        lines = f.read().splitlines()
    drawn_numbers = lines[0].split(",")
    drawn_numbers = [int(x) for x in drawn_numbers]
    print(f"{drawn_numbers=}")
    lines = lines[1:]
    print(f"{lines=}")

    boards = []
    current_board = []

    for line in lines:
        if line:
            current_board.append([int(x) for x in line.split()])
        else:
            current_board = []
            boards.append(current_board)

    print(boards[0])
    print(f"{boards=}")
    print(f"{len(boards)=}")

    bingoBoards = []
    for b in boards:
        bingoBoards.append(Board(b))

    for num in drawn_numbers:
        for b_index, bingboard in enumerate(bingoBoards):
            bingboard.mark_number(num)
            if bingboard.hasBingo():
                print(f"BINGO for {b_index} when drawing {num}" )
                print(bingboard.numbers)
                print(sum(bingboard.numbers))
                return sum(bingboard.numbers) * num
                break
        else:
            continue
        break

class Board:
    def __init__(self, initial_board):
        self.board = initial_board
        self.numbers = sorted([x for y in initial_board for x in y])
        self.bingo_rows = self.create_bingo_rows(self.board)
        print(f"{self.bingo_rows=}")


    def mark_number(self, num):

        self.numbers.remove(num) if num in self.numbers else None
        for row in self.bingo_rows:
            # print(f"{row=}, {num=}")
            row.remove(num) if num in row else None

    def hasBingo(self):
        for i, row in enumerate(self.bingo_rows):
            if len(row) == 0:
                print(f"bingo on row {i}")
                return True


    def create_bingo_rows(self, board):
        rows = []
        cols = [[]]*len(board[0])
        diag1 = []
        diag2 = []
        for row_index, row in enumerate(board):
            for col_index, num in enumerate(row):
                if row_index == col_index:
                    diag1.append(num)
                if (4-row_index) == col_index:
                    diag2.append(num)

                if col_index == 0:
                    rows.append(row)
                if row_index == 0:
                    cols[col_index]= [num]
                else:
                    cols[col_index].append(num)
                print(f"{row_index}:{col_index}::{num}")
        print(f"{rows=}")
        print(f"{cols=}")
        print(f"{diag1=}")
        print(f"{diag2=}")

        toreturn = rows + cols
        # toreturn.append(diag1)
        # toreturn.append(diag2)
        return toreturn

@solver
def part2(test_input=False):
    pass


if __name__ == '__main__':
    assert part1(False) in [4512, 69579]
    # assert part2(False) in [230, 482500]