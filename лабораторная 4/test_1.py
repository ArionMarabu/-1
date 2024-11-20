# TODO решите задачу
import json


def task() -> float:
    sum = 0
    with open("input.json", "r") as read_file:
        data = json.load(read_file)

    for i in range(len(data)):
        sum += data[i]["score"] * data[i]["weight"]

    sum = round(sum, 3)
    return sum


print(task())
