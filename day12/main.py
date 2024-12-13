from typing import List, Tuple
from copy import deepcopy


FILE = "regions.txt"
SIZE = 140

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

VISITED = '-'
VISITING_NOW = "*"


def print_map(region_map: List[str]):
    print("=" * 10)
    for line in region_map:
        print(line)


def add(start: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    return (start[0] + direction[0], start[1] + direction[1])


def set_sign(sign, region_map: List[str], i: int, j: int):
    region_map[i] = region_map[i][:j] + sign + region_map[i][j+1:]


# turns 90 degrees to the right
def turn(direction: Tuple[int, int]) -> Tuple[int, int]:
    directions = [UP, RIGHT, DOWN, LEFT]
    curr_i = directions.index(direction)
    next_i = (curr_i + 1) % len(directions)
    return directions[next_i]


def count_region_price(region_map: List[str],
                       start_i: int, start_j: int, save_history = False) -> int:
    sign = region_map[start_i][start_j]
    area, perimeter = 0, 0
    waiting = [(start_i, start_j)]
    history: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
    for i, j in waiting:
        if region_map[i][j] != VISITING_NOW:
            set_sign(VISITING_NOW, region_map, i, j)
            area += 1
            for direction in [UP, LEFT, RIGHT, DOWN]:
                i2, j2 = add((i, j), direction)
                if not(0 <= i2 < SIZE and 0 <= j2 < SIZE):
                    perimeter += 1
                    history.append(((i2, j2), direction))
                else:
                    if region_map[i2][j2] not in [VISITING_NOW, sign]:
                        perimeter += 1
                        history.append(((i2, j2), direction))
                    if region_map[i2][j2] == sign:
                        waiting.append((i2, j2))
    for i, j in waiting:
        set_sign(VISITED, region_map, i, j)
    if save_history:
        return area * count_sides(history)
    return area * perimeter


def part_one(region_map: List[str], save_history = False) -> int:
    total_price = sum(count_region_price(region_map, i, j, save_history)
                      for i in range(SIZE)
                      for j in range(SIZE)
                      if region_map[i][j] != VISITED)
    print(total_price)


def count_sides(history: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
    sides = 0
    for direction in [UP, LEFT, RIGHT, DOWN]:
        sides_list = [(i, j) if direction in [UP, DOWN] else (j, i)
                      for (i, j), dirr in history
                      if dirr == direction]

        if len(sides_list) > 0:
            sides += 1
            sides_list.sort(key=lambda tup: (tup[0],tup[1]))
            curr_i, last_j = sides_list[0]
            for i, j in sides_list:
                sides += (curr_i != i or j - last_j > 1)
                curr_i, last_j = i, j
    return sides


def part_two(region_map: List[str]) -> int:
    part_one(region_map, True)


def main():
    region_map: List[str] = []
    with open(FILE, "r", encoding='UTF-8') as file:
        region_map = [line.strip() for line in file]
    part_one(deepcopy(region_map))
    part_two(deepcopy(region_map))


if __name__ == "__main__":
    main()
