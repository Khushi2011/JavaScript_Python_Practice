def printhar(string):
    return f"String is:- {string}"

def add(num1, num2):
    return num1 + num2 + 5

print("The name of module is", __name__)

if __name__ == '__main__':
    print(printhar("Khushi Doshi"))
    o = add(4, 6)
    print(o)

