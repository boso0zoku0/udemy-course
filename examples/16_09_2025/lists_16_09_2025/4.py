cash = 350
banknotes_in_atm = [100, 50, 20, 5, 1]


def get_banknote_counts(cash, banknotes_list):
    banknotes_count = []
    
    for banknote in banknotes_list:
        count = cash//banknote
        cash = cash % banknote
        banknotes_count.append(count)
    return banknotes_count



print(get_banknote_counts(cash, banknotes_in_atm))