from typing import List


def part_one():
    fst: List[int] = []
    snd: List[int] = []

    with open("lists.txt") as f: 
        for line in f:
            x = line.split()
            fst.append(x[0])
            snd.append(x[1])

    print(len(fst), len(snd))
    print(fst[0], snd[0])
    print(fst[-1], snd[-1])

    fst.sort()
    snd.sort()
    print(fst[0], snd[0])
    print(fst[-1], snd[-1])

    total: int = 0
    for i in range(1000):
        total += abs(int(fst[i]) - int(snd[i]))

    print(total)


def part_two():
    fst: List[int] = []
    snd: List[int] = []

    with open("lists.txt") as f: 
        for line in f:
            x = line.split()
            fst.append(x[0])
            snd.append(x[1])

    print(len(fst), len(snd))
    print(fst[0], snd[0])
    print(fst[-1], snd[-1])

    fst.sort()
    snd.sort()
    print(fst[0], snd[0])
    print(fst[-1], snd[-1])

    similarity_score: int = 0
    i: int = 0
    for number in fst:
        if i >= len(snd):
            break
        count: int = 0
        while number > snd[i]:
            i += 1
        while number == snd[i]:
            count += 1
            i += 1
        similarity_score += int(number) * count

    print(similarity_score)


def main(): 
    part_one()
    part_two()


if __name__ == "__main__":
    main()