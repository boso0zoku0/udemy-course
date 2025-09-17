from examples.questionnaire.depends import create_password, create_username

db = []


def create_user() -> None:
    user = create_username()
    pas = create_password()
    db.append(user) or db.append(pas)


create_user()
print(db)
