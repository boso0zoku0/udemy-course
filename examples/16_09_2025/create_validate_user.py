# валидация - проверить что строка не пустая или то что не состоит из одних пробелов,
# проверить что введенный текст не является не допустимым выражением(isidentifier)
# реализация: введите имя пользователя - если он введет пробелы, не допустимые символы тогда прервать input и выйти
# точно также с паролем
# если введет правильно то вернуть данные из БД






# def validate_username(username: str):
#     prompt: str = "Введи имя"
#     status: bool = False
#
#     if username.isspace():
#         prompt = "Введите корректные данные\n. Возможно присутствуют лишние пробелы\n"
#
#     elif not username.isidentifier():
#         prompt = "Введите корректные данные\n."
#
#     else:
#         status = True
#     return prompt, status
#
#
# def validate_password(password: str):
#     prompt: str = "Введи пароль"
#     status: bool = False
#
#     if password is False:
#         password = generate_random_password()
#
#     if password.isspace():
#         prompt = "Введите корректные данные\n. Возможно присутствуют лишние пробелы\n"
#
#     elif not password.isidentifier():
#         prompt = "Введите корректные данные\n."
#
#     else:
#         status = True
#     return prompt, status
#
#
# def create_password():
#     prompt: str = "Введите пароль: \n"
#
#     while True:
#         username = input(prompt)
#         prompt, status = validate_username(username)
#         if status:
#             break
#     return username
#
#
# def create_username():
#     prompt: str = "Введите имя: \n"
#
#     while True:
#         username = input(prompt)
#         prompt, status = validate_username(username)
#         if status:
#             break
#     return username

