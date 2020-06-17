# this is going to be my first time making a calculator in python
# ill add comments explaining stuff
print("Calculator \n")
# im just saying that this is a calculator
x = int(input("What is the first number? \n> "))
y = int(input("\n What is the second number? \n> "))
# assigning the two numbers
z = str(input("\n What is the operation? \n(plus, minus, multi, divide) \nOther operations are in these options. \n> "))
# i replaced int() with str() because this is a string
# after this im doing an if chain for the options
# i also nested some more options in the options
# if the user replies with something that isnt recognized it shows an error
if z == "plus":
    a = x + y
elif z == "minus":
    a = x - y
elif z == "multi":
    b = str(input("There are multiple operations for this option. \nmulti - multiply \nexpo - exponents \n> "))
    if b == "multi":
        a = x * y
    elif b == "expo":
        a = x ** y
    else:
        print("ERROR: unexpected input")
elif z == "divide":
    print("There are multiple operations for this option. \nexact - the exact answer \n quo - the quotient ")
    print("\nrem - the remainder \nboth - the quotient and remainder")
    c = str(input("\n> "))
    if c == "exact":
        a = x / y
    elif c == "quo":
        a = x // y
    elif c == "rem":
        a = x % y
    elif c == "both":
        ax = x // y
        ay = x % y
        a = str(ax) + " R " + str(ay)
    else:
        print("ERROR: unexpected input")
else:
    print("ERROR unexpected input")
# i have to turn "a" into a string because of errors (you cant add a str and an int)
aa = "The answer is " + str(a)
print(aa)
