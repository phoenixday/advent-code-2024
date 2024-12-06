from typing import List
import re


def print_puzzle(puzzle: List[str]):
    for line in puzzle:
        print(line)


# 90 degrees on the left
def transpose(puzzle: List[str]) -> List[str]:
    transposed: List[str] = []
    for i in range(len(puzzle)):
        transposed.append("")
        for j in range(len(puzzle[0])):
            transposed[i] += puzzle[j][len(puzzle[0]) - i - 1]
    return transposed


# 45 degrees on the left
def turn_diagonally(puzzle: List[str]) -> List[str]:
    turned: List[str] = []
    for n in range(len(puzzle) + 1):
        new_line = ""
        for i in range(n):
            new_line += puzzle[i][n-i-1]
        turned.append(new_line)
    
    for n in range (len(puzzle)):
        new_line = ""
        s = len(puzzle) - 1
        for i in range(n + 1, len(puzzle)):
            new_line += puzzle[i][s]
            s -= 1 
        turned.append(new_line)
    return turned


def search_horizontal(puzzle: List[str]) -> int:
    count: int = 0
    for line in puzzle:
        xmas = re.findall("XMAS", line)
        count += len(xmas)
    for line in puzzle:
        xmas = re.findall("SAMX", line)
        count += len(xmas)
    return count


# there should be exactly two MASes
def check_for_MASes(square: List[str]) -> bool:
    if square[1][1] != 'A':
        return False
    
    m_count, s_count = 0, 0
    for i in [0, 2]:
        for j in [0, 2]:
            if square[i][j] == 'M':
                m_count += 1
            elif square[i][j] == 'S':
                s_count += 1
            else:
                return False
    
    if not m_count == s_count == 2:
        return False

    return square[0][0] != square[2][2]
    

# each line is 3x3 square
def transform_to_3x3_squares(puzzle: List[str]):
    squares: List[List[str]] = []
    for i in range(len(puzzle) - 2):
        for j in range(len(puzzle[0]) - 2):
            square: List[str] = []
            square.append(puzzle[i][j:j+3])
            square.append(puzzle[i+1][j:j+3])
            square.append(puzzle[i+2][j:j+3])
            squares.append(square)
    # print(squares)
    return squares


def part_one(puzzle: List[str]):
    transposed = transpose(puzzle)
    count: int = search_horizontal(puzzle)
    count += search_horizontal(transpose(puzzle))
    count += search_horizontal(turn_diagonally(puzzle))
    count += search_horizontal(turn_diagonally(transposed))
    print(count)


def part_two(puzzle: List[str]):
    squares = transform_to_3x3_squares(puzzle)
    count: int = 0
    for square in squares:
        if check_for_MASes(square):
            count += 1
    print(count)


def main(): 
    puzzle: List[str] = []
    with open("puzzle.txt", "r") as file:
        for line in file:
            puzzle.append(line[:140])

    part_one(puzzle)
    part_two(puzzle)


if __name__ == "__main__":
    main()