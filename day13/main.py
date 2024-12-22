import re

FILE = "prizes.txt"

A_PRICE = 3
B_PRICE = 1


# from geeks for geeks
def gcd_extended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    # Update x and y using results of recursive call
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


# it's about modular arithmetics, look for linear Diophantine equation.
# it's not well-written, but it works in O(1)
def find_a_b(prize: list[int]) -> tuple[int, int]:
    ax, ay, bx, by = prize[0], prize[1], prize[2], prize[3]
    total_x, total_y = prize[4], prize[5]

    gcdx, x1, x2 = gcd_extended(ax, bx)
    gcdy, _, _ = gcd_extended(ay, by)
    if total_x % gcdx != 0 or total_y % gcdy != 0:
        return -1, -1

    a0 = total_x // gcdx * x1
    b0 = total_x // gcdx * x2
    ag = ax // gcdx
    bg = bx // gcdx

    # we computed a and b for x part, now we want to compute for y part
    k = b0 // ag
    a, b = (a0 + bg * k), (b0 - ag * k)
    start_res = a * ay + b * by
    a, b = (a0 + bg * (k + 1)), (b0 - ag * (k + 1))
    next_res = a * ay + b * by
    diff = next_res - start_res
    i = (total_y - start_res) // diff
    a, b = (a0 + bg * (k + i)), (b0 - ag * (k + i))
    res = a * ay + b * by
    if res == total_y:
        return a, b
    return -1, -1


def part_one(prizes: list[list[int]], bil = False):
    total = 0
    for prize in prizes:
        if bil:
            bil = 10000000000000
            prize[4], prize[5] = prize[4] + bil, prize[5] + bil
        a, b = find_a_b(prize)
        if a != -1:
            total += a * A_PRICE + b * B_PRICE
    print(total)


def part_two(prizes: list[list[int]]):
    part_one(prizes, True)


def main():
    prizes: list[list[int]] = []
    with open(FILE, "r", encoding='UTF-8') as file:
        ax, ay, bx, by, total_x, total_y = 0, 0, 0, 0, 0, 0
        for line in file:
            nums = re.findall(r"\d+", line)
            if len(nums) == 2:
                if ax == 0:
                    ax, ay = int(nums[0]), int(nums[1])
                elif bx == 0:
                    bx, by = int(nums[0]), int(nums[1])
                else:
                    total_x, total_y = int(nums[0]), int(nums[1])
                    prizes.append([ax, ay, bx, by, total_x, total_y])
            else:
                ax, ay, bx, by, total_x, total_y = 0, 0, 0, 0, 0, 0

    part_one(prizes)
    part_two(prizes)


if __name__ == "__main__":
    main()
