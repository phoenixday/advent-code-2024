from typing import List
from math import floor


def check_update(rules: dict[int, List[int]], update: List[int]) -> bool:
    i, j = 0, 1
    for i in range(len(update)):
        num = update[i]
        for j in range(i + 1, len(update)):
             next_num = update[j]
             if (num != next_num) and (not rules.get(num) or (next_num not in rules.get(num))):
                return False 
    return True  
                 

def part_one(rules: dict[int, List[int]], updates: List[List[int]]) -> List[int]:
    count = 0
    incorrect_updates_indices = []
    for i, update in enumerate(updates):
        if check_update(rules, update):
            count += update[floor(len(update) / 2)]
        else:
            incorrect_updates_indices.append(i)
    print(count)
    return incorrect_updates_indices


def correct_order(rules: dict[int, List[int]], update: List[int]):
    was_shuffle = True
    while was_shuffle:
        i, j = 0, 1
        was_shuffle = False
        for i in range(len(update)):
            num = update[i]
            for j in range(i + 1, len(update)):
                next_num = update[j]
                if (num != next_num) and (not rules.get(num) or (next_num not in rules.get(num))):
                    was_shuffle = True
                    update[i], update[j] = update[j], update[i]


def part_two(rules: dict[int, List[int]], updates: List[List[int]], incorrectly_updates_indices: List[int]):
    count = 0
    for i in incorrectly_updates_indices:
        update = updates[i]
        correct_order(rules, update)
        count += update[floor(len(update) / 2)]
    print(count)
    

def read_rule(line: str, rules: dict[int, List[int]]):
    num = int(line.split("|")[0])
    next_num = int(line.split("|")[1])
    if not rules.get(num):
        rules[num] = [next_num]
    else:
        rules[num].append(next_num)


def main(): 
    rules: dict[int, List[int]] = {}
    updates: List[List[int]] = []
    with open("pages.txt", "r") as file:
        for line in file:
            if "|" in line:
                read_rule(line, rules)
            if "," in line:
                nums = line.split(",")
                updates.append([int(num) for num in nums])

    incorrect_updates_indices = part_one(rules, updates)

    part_two(rules, updates, incorrect_updates_indices)

if __name__ == "__main__":
    main()