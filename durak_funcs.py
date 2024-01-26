# функция для преобразования значения в int
def is_int(per):
    try:
        return int(per)
    except ValueError:
        return per


# функция для автоматического зацикливания написания неправильной информации человеком
def auto_error_fix(*params, usl: str = None, message: str = ""):
    print(message, end=message if message == "" else "\n")
    p = ""
    a = []
    for u in params:
        if type(u) == slice:
            for k in range(u.start, u.stop + 1):
                a.append(k)
        else:
            a.append(u)
    while p not in a:
        p = input(usl)
        p = is_int(p)
    return p