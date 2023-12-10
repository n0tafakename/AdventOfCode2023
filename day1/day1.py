#!/usr/bin/python

import sys
import pdb


def find_first_digit(line):
    for c in line:
        if "0" <= c <= "9":
            return int(c)

    raise Exception(f"Failed to find a digit in {line}")


def find_last_digit(line):
    for c in line[::-1]:
        if "0" <= c <= "9":
            return int(c)

    raise Exception(f"Failed to find a digit in {line}")


def part_one(lines):
    calibration_sum = 0
    for line in lines:
        calibration_sum += ((find_first_digit(line) * 10) +
                            find_last_digit(line))

    print(f"Calibration sum: {calibration_sum}")
    return calibration_sum


def find_first_number(line):
    number_strs = ["zero", "one", "two", "three", "four",
                   "five", "six", "seven", "eight", "nine"]
    for i in range(len(line)):
        # is this a digit?
        if "0" <= line[i] <= "9":
            return int(line[i])

        # is this the start of a number string?
        for n, num_str in enumerate(number_strs):
            if (i + len(num_str) < len(line)) and line[i: i + len(num_str)] == num_str:
                return n

    raise Exception(f"Failed to find a number in {line}")


def find_last_number(line):
    number_strs = ["zero", "one", "two", "three", "four",
                   "five", "six", "seven", "eight", "nine"]

    for i in range(len(line) - 1, -1, -1):
        if "0" <= line[i] <= "9":
            return int(line[i])

        for n, num_str in enumerate(number_strs):
            if (i - len(num_str) > -1) and line[i - len(num_str) + 1: i + 1] == num_str:
                return n

    pdb.set_trace()
    raise Exception(f"Failed to find a number in {line}")


def part_two(lines):
    calibration_sum = 0
    for line in lines:
        calibration_sum += ((find_first_number(line) *
                            10) + find_last_number(line))

    print(f"Calibration sum: {calibration_sum}")
    pdb.set_trace()
    return calibration_sum


def main():
    lines = None
    with open("adventofcode.com_2023_day_1_input.txt") as f:
        lines = f.readlines()

    if len(sys.argv) < 2 or sys.argv[1] == "1":
        return part_one(lines)
    else:
        return part_two(lines)


if __name__ == "__main__":
    main()
