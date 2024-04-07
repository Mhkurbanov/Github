from serf import main
x = main()
def plus(a, b):
    return a+b


text = "new function"
def minus(a, b):
    return a-b


if __name__ == "__main__":
    print(plus(23, 46))
    print(minus(80, 45))
    print(x)