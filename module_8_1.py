def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        summ = str(a) + str(b)
        return summ


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
