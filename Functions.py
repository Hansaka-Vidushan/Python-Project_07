def add(*number):
    for x in number:
        if x % 2 == 1:
            print(True)
        else:
            print(False)

def add2(number):
    return number %2 == 1

def add3(number):
    return "Odd" if number % 2 == 1 else "Even"



