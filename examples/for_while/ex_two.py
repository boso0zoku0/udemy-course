# dela = ["Мыть посуду", "Играть в пк", "Позвонить кому то"]
# booll = [True, False, True]
#
# for el in range(len(dela) -1, -1, -1):
#     if booll[el]:
#         mark = "[x]"
#     else:
#         mark = "[ ]"
#     print(f'{el + 1} {mark} {dela[el]}')


dela = [
    ["Мыть посуду", True],
    ["Играть в пк", True],
    ["Позвонить кому то", False],
]
for i in range(len(dela)):
    string = dela[i][0]
    boolean = dela[i][1]
    mark = "[x]" if boolean else "[]"
    print(f"{mark} {string} {boolean}")
