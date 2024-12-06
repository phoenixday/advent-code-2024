from typing import List


def incorrect(curr_distance: int, prev_distance: int) -> bool:
     return not (0 < abs(curr_distance) < 4) \
            or (curr_distance < 0 and prev_distance > 0) \
            or (curr_distance > 0 and prev_distance < 0)


def check_distance(levels: List[int], one_level_tolerated: bool = False) -> bool:
    i: int = 0
    prev_distance: int = 0
    curr_distance: int = 0
    already_tolerated: bool = False
    curr_i: int = 0
    next_i: int = 1
    while next_i < len(levels):
        curr_distance = int(levels[next_i]) - int(levels[curr_i])
        curr_i, next_i = next_i, next_i + 1
        if incorrect(curr_distance, prev_distance): 
                if one_level_tolerated and not already_tolerated:
                    curr_i = curr_i - 1
                    already_tolerated = True
                else:
                    return False
        else: 
            prev_distance = curr_distance

    return True


def part_one():
    safe_reports: int = 0

    with open("reports.txt") as reports: 
        for report in reports:
            levels: List[int] = report.split()
            if check_distance(levels):
                    safe_reports += 1

    print(safe_reports)        


def part_two():
    safe_reports: int = 0

    with open("reports.txt") as reports: 
        for report in reports:
            levels: List[int] = report.split()
            if check_distance(levels[1:]):
                 safe_reports += 1
            else:
                if check_distance(levels, True) or check_distance(levels[::-1], True):
                    safe_reports += 1


    print(safe_reports)  


def main(): 
    part_one()
    part_two()


if __name__ == "__main__":
    main()