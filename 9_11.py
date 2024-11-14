#Задача K
import json

file_in, file_out = input(), input()
numbers = []
with open(file_in) as f:
    for line in f:
        numbers.extend([int(x) for x in line.split()])
data = {
        "count": len(numbers),
        "positive_count": len(list(filter(lambda x: x > 0, numbers))),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2)
}
with open(file_out, "w", encoding="UTF-8") as g:
    json.dump(data, g, ensure_ascii=False, indent=4)