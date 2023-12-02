from pathlib import Path
import re

def day1_1_get_number(line:str) -> int:
    digits = re.findall("\d", line)
    first = int(digits[0])
    last = int(digits[-1])
    return first*10 + last

def day1_1_solution(input:str) -> int:
    numbers = []
    for line in input.split("\n"):
        numbers.append(day1_1_get_number(line))
    return sum(numbers)

def day1_2_replace_spelled_out(input:str) -> str:
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

def day1_2_solution(input:str)->int:
    input = day1_2_replace_spelled_out(input)
    numbers = []
    for line in input.split("\n"):
        numbers.append(day1_1_get_number(line))
    return sum(numbers)


if __name__ == "__main__":

    with open(Path("data") / "day_01" / "input.txt", mode="r", encoding="utf-8") as f:
         input = f.read()
        
    result = day1_2_solution(input)
    print(result)