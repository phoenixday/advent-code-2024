from typing import List, Tuple


FILE = "antennas.txt"
LENGTH = 50

FREE = '.'
ANTINODE = '#'


def add_antinode_to_area(area: List[str], antinode: Tuple[int, int]) -> bool:
    i, j = antinode
    if not (0 <= i < len(area)) or not (0 <= j < len(area[0])) or area[i][j] == ANTINODE:
        return False
    if area[i][j] == FREE:
        area[i] = area[i][:j] + ANTINODE + area[i][j+1:]
    return True


def count_all_antinodes(area: List[str]) -> int:
    return sum(sum(sign != FREE for sign in line) for line in area)


def calculate_two_antinode_positions(fst_antenna: Tuple[int, int], snd_antenna: Tuple[int, int]) \
                                        -> List[Tuple[int, int]]:
    fst_a_i, fst_a_j = fst_antenna
    snd_a_i, snd_a_j = snd_antenna
    vertical_space = abs(fst_a_i - snd_a_i)
    horizontal_space = abs(fst_a_j - snd_a_j)
    fst_i = fst_a_i - vertical_space
    snd_i = snd_a_i + vertical_space
    if fst_i == snd_a_i:
        fst_i = fst_a_i + vertical_space
        snd_i = snd_a_i - vertical_space
    fst_j = fst_a_j - horizontal_space
    snd_j = snd_a_j + horizontal_space
    if fst_j == snd_a_j:
        fst_j = fst_a_j + horizontal_space
        snd_j = snd_a_j - horizontal_space
    return [(fst_i, fst_j), (snd_i, snd_j)]


def calculate_all_antinode_positions(area_size: int, \
                                     fst_antenna: Tuple[int, int], snd_antenna: Tuple[int, int]) \
                                        -> List[Tuple[int, int]]:
    fst_a_i, fst_a_j = fst_antenna
    snd_a_i, snd_a_j = snd_antenna
    vertical_space = abs(fst_a_i - snd_a_i)
    horizontal_space = abs(fst_a_j - snd_a_j)

    fst_i = fst_a_i - vertical_space
    before_i: List[int] = []
    i = fst_a_i
    while 0 <= i < area_size:
        if fst_i != snd_a_i:
            i -= vertical_space
        else:
            i += vertical_space
        before_i.append(i)
    after_i: List[int] = []
    i = snd_a_i
    while 0 <= i < area_size:
        if fst_i != snd_a_i:
            i += vertical_space
        else:
            i -= vertical_space
        after_i.append(i)

    fst_j = fst_a_j - horizontal_space
    before_j: List[int] = []
    j = fst_a_j
    while 0 <= j < area_size:
        if fst_j != snd_a_j:
            j -= horizontal_space
        else:
            j += horizontal_space
        before_j.append(j)
    after_j: List[int] = []
    j = snd_a_j
    while 0 <= j < area_size:
        if fst_j != snd_a_j:
            j += horizontal_space
        else:
            j -= horizontal_space
        after_j.append(j)
    return list(zip(before_i, before_j)) + list(zip(after_i, after_j))


def part_one(area: List[str], antennas: dict[str, List[Tuple[int, int]]], two = True):
    count = 0
    for _, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                fst_antenna, snd_antenna = positions[i], positions[j]
                antinodes = []
                if two:
                    antinodes = calculate_two_antinode_positions(fst_antenna, snd_antenna)
                else:
                    antinodes = calculate_all_antinode_positions(len(area), \
                                                                 fst_antenna, snd_antenna)
                for antinode in antinodes:
                    if add_antinode_to_area(area, antinode):
                        count += 1
    if not two:
        count = count_all_antinodes(area)
    print(count)


def part_two(area: List[str], antennas: dict[str, List[Tuple[int, int]]]):
    part_one(area, antennas, False)


def main():
    area: List[str] = []
    antennas: dict[str, List[Tuple[int, int]]] = {}
    with open(FILE, "r", encoding='UTF-8') as file:
        for i, line in enumerate(file):
            area.append(line[:LENGTH])
            for j, sign in enumerate(line[:LENGTH]):
                if sign != FREE:
                    if sign not in antennas:
                        antennas[sign] = [(i, j)]
                    else:
                        if (i, j) not in antennas[sign]:
                            antennas[sign].append((i, j))
    part_one(area, antennas)
    part_two(area, antennas)


if __name__ == "__main__":
    main()
