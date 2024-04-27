def add(x, y):
    return x + y


result = add(1, 2)
print(f"This is the sum: 1, 2, {result}") # only supported in Python 3.6
print("This is the sum: 1, 2, %s" % result) # for Python 3.5
