from typing import List, Tuple


FILE = "topographic_map.txt"
SIZE = 50

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def add(start: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    return (start[0] + direction[0], start[1] + direction[1])


def find_trailheads(area: List[List[int]], start: Tuple[int, int]) -> set[Tuple[int, int]]:
    start_i, start_j = start
    if area[start_i][start_j] == 9:
        return {start}
    reached: set[Tuple[int, int]] = set()
    for i, j in [add(start, UP), add(start, DOWN), add(start, LEFT), add(start, RIGHT)]:
        if 0 <= i < SIZE and 0 <= j < SIZE and area[i][j] - area[start_i][start_j] == 1:
            reached |= find_trailheads(area, (i, j))
    return reached


def find_ratings(area: List[List[int]], start: Tuple[int, int]) -> int:
    start_i, start_j = start
    if area[start_i][start_j] == 9:
        return 1
    ratings = 0
    for i, j in [add(start, UP), add(start, DOWN), add(start, LEFT), add(start, RIGHT)]:
        if 0 <= i < SIZE and 0 <= j < SIZE and area[i][j] - area[start_i][start_j] == 1:
            ratings += find_ratings(area, (i, j))
    return ratings


def part_one(area: List[List[int]], starts: List[int]):
    total_score = sum(len(find_trailheads(area, start)) for start in starts)
    print(total_score)


def part_two(area: List[List[int]], starts: List[int]):
    total_ratings = sum(find_ratings(area, start) for start in starts)
    print(total_ratings)


def main():
    area: List[List[int]] = []
    starts: List[Tuple[int, int]] = []
    with open(FILE, "r", encoding='UTF-8') as file:
        for i, line in enumerate(file):
            int_line = []
            for j, num in enumerate(line.strip()):
                int_line.append(int(num))
                if num == '0':
                    starts.append((i, j))
            area.append(int_line)
    part_one(area, starts)
    part_two(area, starts)


if __name__ == "__main__":
    main()
