def add(a,b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def substract(a, b):
    print("SUBSTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLY %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just function!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

print("Here is a puzzle.")

# 35 + 74 - 180 * 25
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")