
from pathlib import Path
from enum import Enum
import numpy as np
import numpy.typing as npt
import re

colors = ["red", "green", "blue"]

def get_n_cubes(string:str) -> int:
    num_cubes = int(re.search("\d+", string).group())
    return num_cubes

def get_color(string:str) -> str:
    color = re.search("|".join(colors), string).group()
    return color

def containing_colors(set_:list) -> list:
    colors_list = []
    for string in set_:
        colors_list.append(get_color(string))
    return colors_list

def append_missing_entity(set_:list) -> None:
    colors_list = containing_colors(set_) 
    if len(set_) == 3:
        return set_
    
    for color in colors:
        if color not in colors_list:
            set_.append(f"0 {color}")

def color_sorter(string:str) -> int:
    color = get_color(string)
    sorting = {
        "red":1,
        "green":2,
        "blue":3
    }
    return sorting[color]

def assembly_games_array(input:str) -> np.ndarray:
    games = []
    for game in input.split("\n"):
        sets_string = game.split(": ")[1].split(";")
        sets = []
        for set_string in sets_string:
            set_ = set_string.split(",")
            append_missing_entity(set_)
            set_ = sorted(set_, key=color_sorter) # order: red, green, blue
            sets.append([get_n_cubes(elem) for elem in set_])
        games.append(np.array(sets).flatten())
    max_num_elements = len(max(games, key=len))
    games_array = np.zeros((len(games), max_num_elements))
   
    for i, game in enumerate(games):
        games_array[i, :len(game)] = game
    return games_array

def get_color_columns(games_array:npt.NDArray[np.int64], index:int=0) -> npt.NDArray[np.int64]:
    cols = np.array(range(0,games_array.shape[1], 3))+index
    return games_array[:, cols]

def solution_1(input:str) -> int:
    games_array = assembly_games_array(input)
    reds = get_color_columns(games_array, index=0)
    greens = get_color_columns(games_array, index=1)
    blues = get_color_columns(games_array, index=2)

    mask = (reds<=12) & (greens<=13)  & (blues<=14)
    return np.sum(np.where(np.all(mask, axis=1))[0]+1)

def solution_2(input:str) -> int:
    games_array = assembly_games_array(input)
    reds = get_color_columns(games_array, index=0)
    greens = get_color_columns(games_array, index=1)
    blues = get_color_columns(games_array, index=2)

    power = np.max(reds, axis=1) * np.max(greens, axis=1) * np.max(blues, axis=1) 
    return np.sum(power).astype(int)


if __name__ == "__main__":
    with open(Path("data") / "day_02" / "input.txt", mode="r", encoding="utf-8") as f:
         input = f.read()
        
    sol_1 = solution_1(input)
    print("Puzzle 1: ", sol_1)

    sol_2 = solution_2(input)
    print("Puzzle 2: ", sol_2)

