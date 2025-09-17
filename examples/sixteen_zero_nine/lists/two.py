temps_celsius = [
    -1.5,
    0.2,
    2.8,
    5.6,
    8.4,
    11.2,
    14.7,
    17.0,
    18.3,
    19.1,
    19.4,
    18.8,
    17.0,
    14.5,
    11.2,
    7.8,
    4.0,
]
temps_celsius2 = [-1.5, 0.2, 2.8, 5.6, 8.4, 11.2, 14.7, 17.0, 14.5, 11.2, 7.8, 4.0]

# def average_value(*nums, rounding: int = 2):
#     for num in nums:
#         if num:
#             len_el = len(num)
#             summ_el = sum(num)
#             middle_num = summ_el / len_el
#             print(middle_num)
#
# print(average_value(temps_celsius))


def average_value(*nums, rounding=2) -> float | None:
    if nums:
        len_el = len(nums)
        summ_el = sum(nums)
        middle_num = summ_el / len_el
        return round(middle_num, rounding)
    return None


print(average_value(*temps_celsius))
