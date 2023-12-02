from day_01 import *


def test_solution_1():
    input = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    assert 142 == solution_1(input)

def test_get_number():
    input = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"

    lines = input.split("\n")   
    results = [12, 38, 15, 77]

    for line,result in zip(lines, results):
        assert get_number(line) == result

def test_replace_spelled_out():
    input = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
    input = replace_spelled_out(input)
    lines = input.split("\n")   
    results = [29, 83, 13, 24, 42, 14,76]

    for line,result in zip(lines, results):
        assert get_number(line) == result

def test_solution_2():
    input = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"

    assert 281 == solution_2(input)