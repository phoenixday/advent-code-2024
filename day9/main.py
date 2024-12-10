from typing import List
import itertools

FILE = "disk_map.txt"
FREE = -1


def to_str(int_arr: List[int]):
    str_arr = ""
    for i in int_arr:
        str_arr += "." if i == FREE else str(i)
    print(str_arr)


def convert_to_full_format(disk_map: str) -> List[int]:
    full_map = ""
    not_free = True
    i = 0
    for length in disk_map:
        if not_free:
            full_map = itertools.chain(full_map, [i for _ in range(int(length))])
            i += 1
        else:
            full_map = itertools.chain(full_map, [FREE for _ in range(int(length))])
        not_free = not not_free
    return list(full_map)


def move_files_to_the_left(full_map: List[int]) -> List[int]:
    # we will swap indices instead of swaping right inside the string
    indices = list(range(len(full_map)))
    start, end = 0, len(full_map) - 1
    while start < end:
        while start < end and full_map[start] != FREE:
            start += 1
        while end > start and full_map[end] == FREE:
            end -= 1
        indices[start], indices[end] = indices[end], indices[start]
        start += 1
        end -= 1
    swaped_map = []
    for i in indices:
        swaped_map.append(full_map[i])
    return swaped_map


def move_whole_files_to_the_left(full_map: List[int]):
    num_lengths, num_indices = [], []
    free_lengths, free_indices = [], []
    i = 0
    while i < len(full_map):
        num = full_map[i]
        num_i = i
        while i < len(full_map) and full_map[i] == num:
            i += 1
        if num == FREE:
            free_lengths.append(i - num_i)
            free_indices.append(num_i)
        else:
            num_lengths.append(i - num_i)
            num_indices.append(num_i)

    for i in range(len(num_indices) - 1, -1, -1):
        curr_length, curr_i = num_lengths[i], num_indices[i]
        for j, free_length in enumerate(free_lengths):
            if free_indices[j] >= curr_i:
                break
            if free_length >= curr_length:
                for l in range(curr_length):
                    full_map[curr_i + l], full_map[free_indices[j] + l] \
                        = full_map[free_indices[j] + l], full_map[curr_i + l]
                free_lengths[j] -= curr_length
                free_indices[j] += curr_length
                num_lengths[i] -= curr_length
                break


def calculate_checksum(swaped_map: List[int]) -> int:
    checksum = 0
    for position, file_id in enumerate(swaped_map):
        if file_id != FREE:
            checksum += position * file_id
    return checksum


def part_one(disk_map: str) -> int:
    full_map = convert_to_full_format(disk_map)
    swaped_map = move_files_to_the_left(full_map)
    print(calculate_checksum(swaped_map))


def part_two(disk_map: str) -> int:
    full_map = convert_to_full_format(disk_map)
    move_whole_files_to_the_left(full_map)
    print(calculate_checksum(full_map))


def main():
    disk_map: str = []
    with open(FILE, "r", encoding='UTF-8') as file:
        disk_map = file.readline()
    part_one(disk_map)
    part_two(disk_map)


if __name__ == "__main__":
    main()
