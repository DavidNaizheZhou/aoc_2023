from pathlib import Path
import numpy as np


def assembly_games_array(input_: str) -> np.ndarray:
    lines = input_.split("\n")
    winning_nums = []
    numbers = []
    for game in lines:
        game_str = game.split(": ")[1]
        winning_nums.append(np.fromstring(game_str.split("|")[0], dtype=int, sep=" "))
        numbers.append(np.fromstring(game_str.split("|")[1], dtype=int, sep=" "))

    return np.vstack(winning_nums), np.vstack(numbers)


def intersect_along_axis(row, width):
    return np.in1d(row[:width], row[width:]).astype(int)


def points(winning_nums, numbers):
    isin_array = np.apply_along_axis(
        func1d=intersect_along_axis,
        axis=1,
        arr=np.hstack([numbers, winning_nums]),
        width=numbers.shape[1],
    )

    power = np.sum(isin_array, axis=1)
    factor = power > 0
    power = power - 1
    power[power <= 0] = 0
    score = np.sum(2 ** (power) * factor)
    return score


def calc_copies(num_match, num_cards):
    array = np.zeros_like(num_match)
    for i, num in enumerate(num_match):
        for j in range(num_cards[i]):
            array[i + 1 : i + 1 + num] += 1
    if np.sum(array) != 0:
        array += calc_copies(num_match, array)
    return array


def num_scratchcards(winning_nums, numbers):
    isin_array = np.apply_along_axis(
        func1d=intersect_along_axis,
        axis=1,
        arr=np.hstack([numbers, winning_nums]),
        width=numbers.shape[1],
    )
    num_match = np.sum(isin_array, axis=1)
    copies = calc_copies(num_match, num_cards=np.ones_like(num_match)) + 1
    return np.sum(copies)


def solution_1(input_):
    winning_nums, numbers = assembly_games_array(input_)
    return points(winning_nums, numbers)


def solution_2(input_):
    winning_nums, numbers = assembly_games_array(input_)
    return num_scratchcards(winning_nums, numbers)


if __name__ == "__main__":
    with open(Path("data") / "day_04" / "input.txt", mode="r", encoding="utf-8") as f:
        input_ = f.read()

    sol_1 = solution_1(input_)
    print("Puzzle 1: ", sol_1)

    sol_2 = solution_2(input_)
    print("Puzzle 2: ", sol_2)
