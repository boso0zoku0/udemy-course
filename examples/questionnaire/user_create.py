from examples.questionnaire.depends import create_username, create_password
db = []


def create_user():
    user = create_username()
    pas = create_password()
    db.append(user) or db.append(pas)


create_user()
print(db)
