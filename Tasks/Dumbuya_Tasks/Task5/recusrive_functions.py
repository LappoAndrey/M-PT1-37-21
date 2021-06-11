inner_lists = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def adding_values(y):
    if len(y) <= 1:
        return y[0]
    else:
        return sum(adding_values(number) if isinstance(number, list) else number for number in y)


r = adding_values(inner_lists)
print(r)
