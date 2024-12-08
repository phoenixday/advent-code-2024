from typing import List


def calculate(res: int, nums: List[int], i: int, concat = False) -> int:
    if i == 1:
        if res == nums[i]:
            return res
        return -1
    sub_res = res - nums[i]
    if sub_res > 0 and sub_res == calculate(sub_res, nums, i - 1, concat):
        return res
    div_res = res // nums[i]
    if res % nums[i] == 0 and div_res == calculate(div_res, nums, i - 1, concat):
        return res
    if concat and sub_res > 0:
        tens = pow(10, len(str(nums[i])))
        concat_res = sub_res // tens
        if sub_res % tens == 0 and concat_res == calculate(concat_res, nums, i - 1, concat):
            return res
    return -1


def part_one(equations: List[List[int]], concat = False):
    total = 0
    for eq in equations:
        if calculate(eq[0], eq, len(eq) - 1, concat) == eq[0]:
            total += eq[0]
    print(total)


def part_two(equations: List[List[int]]):
    part_one(equations, True)


def main():
    equations: List[List[int]] = []
    with open("equations.txt", "r", encoding='UTF-8') as file:
        for line in file:
            equations.append(
                [int(num) if i > 0 else int(num[:-1])
                 for i, num in enumerate(line.split())])
    part_one(equations)
    part_two(equations)


if __name__ == "__main__":
    main()
