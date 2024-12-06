from typing import List
import re


def calculate_muls(puzzle: str) -> int:
    muls: List[str] = re.findall("mul\(\d{1,3},\d{1,3}\)", puzzle)
    total: int = 0
    for mul in muls:
        n1, n2 = re.split(",", mul[4:-1])
        total += int(n1) * int(n2)
    return total


def part_one(puzzle: str):
   print(calculate_muls(puzzle))


def part_two(puzzle: str):
    donts = re.split("don't\(\)", puzzle) 
    res: str = donts[0]
    for dont in donts[1:]:
        do = re.split("do\(\)", dont) 
        res += "".join(do[1:])
    print(calculate_muls(res))


def main(): 
    puzzle: str = ""
    with open("puzzle.txt", "r") as file:
        puzzle = file.read()
    part_one(puzzle)
    part_two(puzzle)


if __name__ == "__main__":
    main()