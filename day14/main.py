FILE = "robots.txt"

WIDE = 101
TALL = 103

SECONDS = 100
MORE_SECONDS = 100000


def print_bathroom(bathroom: list[list[int]], sec: int):
    with open("bathroom.txt", "a", encoding='UTF-8') as file:
        file.write(str(sec) + "\n")
        for line in bathroom:
            file.write(''.join(['.' if j == 0 else str(j) for j in line]) + "\n")
        file.write("\n")


# def find_final_position(robot: tuple[int, int, int, int]) -> tuple[int, int]:
#     x, y, vx, vy = robot
#     for _ in range(SECONDS):
#         x = (x + vx) % WIDE
#         y = (y + vy) % TALL
#     return x, y


def robots_in_quadrant(bathroom: list[list[int]],
                       start_i: int, end_i: int, start_j: int, end_j: int) -> int:
    robots = 0
    for i in range(start_i, end_i):
        robots += sum(bathroom[i][start_j: end_j])
    return robots


def count_safety_factor(bathroom: list[list[int]]) -> int:
    safety_factor = 1
    safety_factor = safety_factor * robots_in_quadrant(bathroom, 0, TALL // 2, 0, WIDE // 2)
    safety_factor = safety_factor * robots_in_quadrant(bathroom, 0, TALL // 2, WIDE // 2 + 1, WIDE)
    safety_factor = safety_factor * robots_in_quadrant(bathroom, TALL // 2 + 1, TALL, 0, WIDE // 2)
    safety_factor = safety_factor * robots_in_quadrant(bathroom, TALL // 2 + 1,
                                                       TALL, WIDE // 2 + 1, WIDE)
    return safety_factor


def part_one(robots: list[list[int, int, int, int]], save_factors = False) -> int:
    bathroom: list[list[int]] = [[0 for _ in range(WIDE)] for _ in range(TALL)]
    smallest_safety_factor, sec = 10000000000, 0
    for s in range(SECONDS if not save_factors else MORE_SECONDS):
        for i, robot in enumerate(robots):
            x, y, vx, vy = tuple(robot)
            if bathroom[y][x] > 0:
                bathroom[y][x] = bathroom[y][x] - 1
            x = (x + vx) % WIDE
            y = (y + vy) % TALL
            robots[i] = [x, y, vx, vy]
            bathroom[y][x] = bathroom[y][x] + 1
        if save_factors:
            safety_factor = count_safety_factor(bathroom)
            if safety_factor < smallest_safety_factor:
                smallest_safety_factor = safety_factor
                sec = s
                print_bathroom(bathroom, s + 1)
            # for some reason, this was an accepted answer,
            # even if the correct asnwer was 7243
            if s == 7343:
                print_bathroom(bathroom, s + 1)
    if not save_factors:
        print(count_safety_factor(bathroom))
    else:
        print(sec + 1)


# with the help of
# https://www.reddit.com/r/adventofcode/comments/1heayz8/2024_day_14_part_2_this_kind_of_rocks/
def part_two(robots: list[list[int, int, int, int]]):
    part_one(robots, True)


def main():
    robots: list[list[int, int, int, int]] = []
    with open(FILE, "r", encoding='UTF-8') as file:
        for line in file:
            p = line.split()[0][2:].split(',')
            v = line.split()[1][2:].split(',')
            robots.append([int(p[0]), int(p[1]), int(v[0]), int(v[1])])

    part_one(robots)
    part_two(robots)


if __name__ == "__main__":
    main()
