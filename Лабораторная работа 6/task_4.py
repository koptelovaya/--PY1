import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",") -> list[dict]:
    with open(filename, 'r') as file:
        head_list = file.readline()[:-1].split(delimiter)
        rows_list = [line[:-1].split(delimiter) for line in file.readlines()]
        return [dict(zip(head_list, line)) for line in rows_list]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
