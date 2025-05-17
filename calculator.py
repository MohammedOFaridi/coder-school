def calculator(x, y, op):
    if op == ("+"):
        z = x + y
        return z
    elif op == ("-"):
        z = x - y
        return z
    elif op == ("x"):
        z = x * y
        return z
    elif op == ("/"):
        z = x / y
        return z
    else:
        print("system faliure. try printing +, -, x, or / in symbol")


f = int(input("number 1 "))
g = int(input("number 2 "))
op = input("Choose between + , - , x , or / ")
print(calculator(f, g, op))
#thisis a calculator
