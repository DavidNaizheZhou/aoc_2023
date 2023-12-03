import numpy as np
from pathlib import Path
import re

def convert_input(input):
    return np.array([list(line) for line in input.split("\n")])

def find_numbers(line):
    positions = []
    numbers = []
    for result in re.compile("\d+").finditer(line):
        positions.append(result.span())
        numbers.append(result.group())
    return np.array(numbers, dtype=int), np.array(positions, dtype=int)

def get_adjacent_indices(row, col_start, col_end, input_shape):
    len_ = col_end-col_start
    num_adjacent = 2*(len_+3) 
    rows = np.empty(num_adjacent, dtype=int)
    cols = np.empty(num_adjacent, dtype=int)
    rows[:len_+2], cols[:len_+2] = row-1, range(col_start-1, col_end+1)
    rows[len_+2:len_+4], cols[len_+2:len_+4] = row, (col_start-1, col_end)
    rows[len_+4:], cols[len_+4:] = row+1, range(col_start-1, col_end+1)
    mask = (rows>=0) & (cols>=0) & (rows<input_shape[0]) & (cols<input_shape[1])
    return rows[mask], cols[mask]

def sum_condition(array):
    array[array=="."] = "a"
    issymbol = ~np.char.isalnum(array) 
    return np.any(issymbol)

def star_mask(array):
    return array=="*"

def star_condition(array):
    return np.any(array=="*")

def solution_1(input):
    input_array = convert_input(input)
    numbers_list = []
    for i, line in enumerate(input.split("\n")):
        numbers, positions = find_numbers(line)
        for number, position in zip(numbers, positions):
            adjacent = get_adjacent_indices(i, *position, input_array.shape)

            if sum_condition(input_array[adjacent]):
                numbers_list.append(number)
    return sum(numbers_list)

def get_bounding_box(adjacent):
    return [np.min(adjacent[0]), np.max(adjacent[0]),np.min(adjacent[1]), np.max(adjacent[1])]

def solution_2(input):
    input_array = convert_input(input)
    adjacents = []
    numbers_list = []
    for i, line in enumerate(input.split("\n")):
        numbers, positions = find_numbers(line)
        for number, position in zip(numbers, positions):
            adjacent = get_adjacent_indices(i, *position, input_array.shape)
            if star_condition(input_array[adjacent]):
                mask = input_array[adjacent] == "*"
                star_pos = [adjacent[0][mask][0], adjacent[1][mask][0]]
                numbers_list.append(number)
                adjacents.append(star_pos)

    adjacents = np.array(adjacents)
    numbers_list = np.array(numbers_list)
    unique, indices, counts = np.unique(adjacents, return_counts=True, return_index=True, axis=0)
    mask = counts>1

    sum_gear_ratios = 0
    for val in unique[mask]:
        indices = np.where((adjacents == val).all(axis=1))
        sum_gear_ratios += np.prod(numbers_list[indices[0]])
    return sum_gear_ratios

if __name__ == "__main__":
    with open(Path("data") / "day_03" / "input.txt", mode="r", encoding="utf-8") as f:
         input = f.read()
        
    sol_1 = solution_1(input)
    print("Puzzle 1: ", sol_1)

    sol_2 = solution_2(input)
    print("Puzzle 2: ", sol_2)