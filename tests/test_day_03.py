import day_03
from pytest import fixture
import numpy as np

@fixture
def example():
    input = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."
    return input

@fixture
def example2():
    input = ".100\n...."
    return input

def test_get_adjacent_indices(example2):
    input_array = day_03.convert_input(example2)
    adjacent = day_03.get_adjacent_indices(0,1,4,input_array.shape)
    assert len(input_array[adjacent]) == 5
    assert np.all(input_array[adjacent] == '.')

def test_is_digit(example2):
    input_array = day_03.convert_input(example2)
    adjacent = day_03.get_adjacent_indices(0,1,4,input_array.shape)
    assert len(input_array[adjacent]) == 5
    assert np.all(input_array[adjacent] == '.')

def test_sum_condition():
    assert day_03.sum_condition(np.array([".", "$"])) == True
    assert day_03.sum_condition(np.array([".", "."])) == False
    assert day_03.sum_condition(np.array(["0", "0"])) == False

def test_solution_1(example):
    assert day_03.solution_1(example) == 4361

def test_solution_2(example):
    assert day_03.solution_2(example) == 467835