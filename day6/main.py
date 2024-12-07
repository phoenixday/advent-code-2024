from typing import List, Tuple
import re


LENGTH = 130

BORDER = '*'
WALL = '#'
FREE = '.'
UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)


def add(fst: Tuple[int, int], snd: Tuple[int, int]) -> Tuple[int, int]:
    return fst[0] + snd[0], fst[1] + snd[1]


def get_direction(dir_char: str) -> Tuple[int, int]:
    dir_chars = "^>v<"
    directions = [UP, RIGHT, DOWN, LEFT]
    curr_i = dir_chars.index(dir_char)
    return directions[curr_i]


def get_direction_sign(direction: Tuple[int, int]) -> str:
    dir_chars = "^>v<"
    directions = [UP, RIGHT, DOWN, LEFT]
    curr_i = directions.index(direction)
    return dir_chars[curr_i]


def get_sign(area: List[str], position: Tuple[int, int]) -> str:
    i, j = position
    return area[i][j]


def visit(area: List[str], position: Tuple[int, int], direction: Tuple[int, int]):
    sign = get_direction_sign(direction)
    i, j = position
    area[i] = area[i][:j] + sign + area[i][j+1:]


# turns 90 degrees on the right
def turn(direction: Tuple[int, int]) -> Tuple[int, int]:
    directions = [UP, RIGHT, DOWN, LEFT]
    curr_i = directions.index(direction)
    next_i = (curr_i + 1) % len(directions)
    return directions[next_i]


def part_one(area: List[str], position: Tuple[int, int], direction: Tuple[int, int]):
    count = 0
    while True:
        if get_sign(area, position) == FREE:
            count += 1
        visit(area, position, direction)
        while get_sign(area, add(position, direction)) == WALL:
            direction = turn(direction)
        if get_sign(area, add(position, direction)) == BORDER:
            break
        position = add(position, direction)
    print(count)


# check: if i will turn right from current cell, then i will not get into cycle
def check_loop(area: List[str], start_position: Tuple[int, int], start_direction: Tuple[int, int]) -> Tuple[int, int]:
    position, direction = start_position, start_direction
    history_map: List[List[str]] = [[[] for _ in line] for line in area] # we want to remember all the history
    for i, line in enumerate(area):
        for j, sign in enumerate(line):
            if sign in [WALL, BORDER]:
                history_map[i][j].append(sign)

    next_i, next_j = add(position, direction)
    history_map[next_i][next_j] = [WALL] # let's put a WALL just in front of us

    while True:
        curr_i, curr_j = position
        dir_sign = get_direction_sign(direction)
        if BORDER in history_map[curr_i][curr_j]:
            return (-1, -1)
        if dir_sign in history_map[curr_i][curr_j]:
            return add(start_position, start_direction)
        history_map[curr_i][curr_j].append(dir_sign)
        next_i, next_j = add(position, direction)
        while WALL in history_map[next_i][next_j]:
            direction = turn(direction)
            next_i, next_j = add(position, direction)
        position = (next_i, next_j)


def part_two(area: List[str], position: Tuple[int, int], direction: Tuple[int, int]):
    obstacles: List[Tuple[int, int]] = []
    while True:
        while get_sign(area, add(position, direction)) == WALL:
            direction = turn(direction)
        visit(area, position, direction)
        if get_sign(area, add(position, direction)) == BORDER:
            break
        obst = check_loop(area, position, direction)
        if obst != (-1, -1) and get_sign(area, obst) == FREE and obst not in obstacles:
            obstacles.append(obst)
        position = add(position, direction)      
    print(len(obstacles))


def main():
    area: List[str] = [""]
    start_position: Tuple[int, int] = (-1, -1)
    start_direction: Tuple[int, int] = UP
    with open("map.txt", "r", encoding='UTF-8') as file:
        for i, line in enumerate(file):
            if start_position == (-1, -1):
                starts_here = re.search("[^.#\n]", line)
                if starts_here:
                    j = starts_here.start()
                    start_position = (i + 1, j + 1)
                    start_direction = get_direction(line[j])
                    line = re.sub("[^.#\n]", FREE, line)
            area.append(BORDER + line[:LENGTH] + BORDER) # add side borders

    # add upper/down borders
    area[0] = BORDER * (LENGTH + 2)
    area.append(area[0])

    # part_one(area, start_position, start_direction)
    part_two(area, start_position, start_direction) # takes some times


if __name__ == "__main__":
    main()
