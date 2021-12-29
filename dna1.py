from sys import argv, exit
import csv


def getMaxNumOfTimesStrs(s, strs):
    index = [0] * len(s)

    for i in range(len(s) - len(strs), -1, -1):
        if s[i: i + len(strs)] == strs:
            if i + len(strs) > len(s) - 1:
                index[i] = 1

            else:
                index[i] = 1 + index[i + len(strs)]
    return max(index)


def print_match(reader, real):
    for line in reader:
        people = line[0]
        outputs = [int(out) for out in line[1:]]

        if outputs == real:
            print(people)
            return
    print("No match")


def main():
    if len(argv) != 3:
        print("Usage: Python dna.py data.csv sequence.txt")
        exit(1)

    csv_path = argv[1]
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        total_sequence = next(reader)[1:]

        txt_path = argv[2]
        with open(txt_path) as txt_file:
            s = txt_file.read()
            real = [getMaxNumOfTimesStrs(s, seq) for seq in total_sequence]

        print_match(reader, real)


if __name__ == "__main__":
    main()
