oper = {
             '+': (1, lambda x, y: x + y),
             '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y),
             '/': (2, lambda x, y: x / y), 
        }


def parsing(formula):
    numb = ''
    for i in formula:
        if i in '0123456789.':
            numb += i
        elif numb:
            yield float(numb)
            numb = ''
        if i in oper or i in "()":
            yield i
    if numb:
        yield float(numb)

def sort(formula_after_parsing):
    stack = []
    for token in formula_after_parsing:
        if token in oper:
            while stack and stack[-1] != "(" and oper[token][0] <= oper[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            stack.append(token)
        else:
            yield token
    while stack:
        yield stack.pop()

def calc(formula_after_sort):
    stack = []
    for token in formula_after_sort:
        if token in oper:
            y, x = stack.pop(), stack.pop()
            stack.append(oper[token][1](x, y))
        else:
            stack.append(token)
    return stack[0]
