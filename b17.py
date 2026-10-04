data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]

diem_theo_ten = {}
for muc in data:
    ten = muc["name"]
    diem = muc["score"]
    if ten not in diem_theo_ten:
        diem_theo_ten[ten] = []
    diem_theo_ten[ten].append(diem)

print(diem_theo_ten)