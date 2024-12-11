from typing import List, Tuple


FILE = "stones.txt"


def change(stone: int) -> List[int]:
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        fst = int(str(stone)[:half])
        snd = int(str(stone)[half:])
        return [fst, snd]
    return [stone * 2024]


def calculate_stone(stone: int, stone_dict: dict[int, List[int]], blinks: int) -> int:
    ch = change(stone)
    if blinks == 1:
        if (stone, blinks) in stone_dict:
            return stone_dict[(stone, blinks)]
        stone_dict[(stone, blinks)] = len(ch)
        return len(ch)
    count = 0
    for st in ch:
        if (st, blinks) in stone_dict:
            count += stone_dict[(st, blinks)]
        else:
            res = calculate_stone(st, stone_dict, blinks - 1)
            count += res
            stone_dict[(st, blinks)] = res
    return count


def part_one(stones: List[int], blinks = 25) -> int:
    count = 0
    stone_dict: dict[Tuple[int, int], int] = {}
    for stone in stones:
        if (stone, blinks) in stone_dict:
            count += stone_dict[(stone, blinks)]
        else:
            res = calculate_stone(stone, stone_dict, blinks)
            count += res
            stone_dict[(stone, blinks)] = res
    print(count)


def part_two(stones: List[int], blinks: int):
    part_one(stones, blinks)


def main():
    stones: List[int] = []
    with open(FILE, "r", encoding='UTF-8') as file:
        stones = [int(num) for num in file.readline().split()]
    part_one(stones)
    part_two(stones, 75)


if __name__ == "__main__":
    main()
