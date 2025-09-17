currencies = [
    ("USD", "United States Dollar"),
    ("EUR", "Germany"),
    ("JPY", "Japan"),
    ("AUD", "Australia"),
    ("SEK", "Sweden"),
]

for i in range(len(currencies) - 1, -1, -1):
    if currencies[i][0] == "USD":
        currencies.pop(i)
        print(f"Deleted {currencies[i][1]}")
print(currencies)


#
# words = ("привет", "как", "дела")
# symbol_v = words[0][3]  # Привет -> второй символ (индексация начинается с нуля)
# print(symbol_v)  # выведет "в"
