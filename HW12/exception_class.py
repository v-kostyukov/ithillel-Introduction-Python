class TokenErr(Exception):
    msg = "Invalid token!"

    def __init__(self, value=None):
        if value is not None:
            self.msg = value

    def __str__(self):
        return self.msg


def f_token(token):
    pass_token = 'qwerty123'

    try:
        if token != pass_token:
            raise TokenErr("Incorrect token!")
    except TokenErr as error:
        print(error.__str__())


t = input("Введите токен: ")
f_token(t)
