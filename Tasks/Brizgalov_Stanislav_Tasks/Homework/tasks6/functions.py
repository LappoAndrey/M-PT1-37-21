prior = {"(": 0,
         ")": 0,
         "+": 1,
         "-": 1,
         "*": 2,
         "/": 2
    }

current_number = []
current_oper = []


def calc(last_current_oper):
    global current_number
    global current_oper
    x = current_number.pop()
    y = current_number.pop()
    if last_current_oper[-1] == "-":
        return current_number.append(y - x), current_oper.pop()
    elif last_current_oper[-1] == "+":
        return current_number.append(y + x), current_oper.pop()
    elif last_current_oper[-1] == "*":
        return current_number.append(y * x), current_oper.pop()
    elif last_current_oper[-1] == "/":
        return current_number.append(y / x), current_oper.pop()


def main(arith):
    for index, el in enumerate(arith):
        if el.isdigit():
            if arith[index-1].isdigit() and index != 0:
                a = str(current_number.pop())
                current_number.append(int(a+el))
            else:
                current_number.append(int(el))
        elif el == "-" and (index == 0 or arith[index-1] == "("):
            current_number.append(-1)
            current_oper.append("*") 
        elif el == "(":
            current_oper.append(el)
        elif el == ")":
            while prior.get(current_oper[-1]) != 0:
                calc(current_oper[-1])
            else: 
                if el == ")" and current_oper[-1] == "(":
                    current_oper.pop()
        elif current_oper == []:
            current_oper.append(el)
        elif current_oper:
            while current_oper and prior.get(el) <= prior.get(current_oper[-1]) and len(current_number) >= 2:
                calc(current_oper[-1])
            current_oper.append(el)
    while current_oper:
        calc(current_oper[-1])
    return current_number[0] 