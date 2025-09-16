votes = ["Да", "Нет", "Да", "Да", "Воздержался", "Нет", "Да"]

types = ["Да", "Нет", "Воздержался"]
result = []

for vote_type in types:
    count = 0
    for v in votes:
        if v == vote_type:
            count += 1
    result.append((vote_type, count))

print(result)


x = list(range(-1, 52, 2))
print(x)