from pathlib import Path
import re

def get_number(line:str) -> int:
    digits = re.findall("\d", line)
    first = int(digits[0])
    last = int(digits[-1])
    return first*10 + last

def solution_1(input:str) -> int:
    numbers = []
    for line in input.split("\n"):
        numbers.append(get_number(line))
    return sum(numbers)

def replace_spelled_out(input:str) -> str:
    input = input.lower()
    mapping = {
            "zero":"z0ro",
            "one":"o1e",
            "two":"t2o",
            "three":"th3ee",
            "four":"f4ur",
            "five":"f5ve",
            "six":"s6x",
            "seven":"se7en",
            "eight":"ei8ht",
            "nine":"n9ne",
    }

    for key, value in mapping.items():
        input = input.replace(key, value)
    return input

def solution_2(input:str)->int:
    input = replace_spelled_out(input)
    numbers = []
    for line in input.split("\n"):
        numbers.append(get_number(line))
    return sum(numbers)


if __name__ == "__main__":

    with open(Path("data") / "day_01" / "input.txt", mode="r", encoding="utf-8") as f:
         input = f.read()
        
    result = solution_2(input)
    print(result)