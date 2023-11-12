import json

# TODO решите задачу
def task(json_file) -> float:
    with open(json_file) as file:
        data = json.load(file)
    product_sum = sum([item["score"] * item["weight"] for item in data])
    return round(product_sum, 3)

json_file = "input.json"
print(task(json_file))
