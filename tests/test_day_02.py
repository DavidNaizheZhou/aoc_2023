import day_02
from pytest import fixture
import numpy as np

@fixture
def example():
    input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    return input


def test_cube_properties(example):
    assert day_02.get_color(" 3 blue ") == "blue"
    assert day_02.get_n_cubes(" 4 red") == 4
    assert day_02.get_n_cubes(" 20 red") == 20
    assert day_02.get_n_cubes(" 200 red") == 200

def test_solution_1(example):
    assert day_02.solution_1(example) == 8

def test_solution_2(example):
    assert day_02.solution_2(example) == 2286