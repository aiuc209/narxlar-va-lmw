mahsulotlar = [
    {"nomi": "Apple", "narxi": 10000, "miqdori": 5},
    {"nomi": "Banana", "narxi": 5000, "miqdori": 10},
    {"nomi": "Orange", "narxi": 8000, "miqdori": 7}
]

umumiy_qiymatlar = {mahsulot["nomi"]: mahsulot["narxi"] * mahsulot["miqdori"] for mahsulot in mahsulotlar}

for nomi, qiymat in umumiy_qiymatlar.items():
    print(f"{nomi}: {qiymat}")
