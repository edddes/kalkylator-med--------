num1 = input("ditt första nummer: ")
variable = input("skriv in ditt räknesätt (+, -, *, /): ")
num2 = input("ditt andra nummer: ")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)

if variable == "+":
    print(add)

elif variable == "-":
    print(subtract)

elif variable == "*":
    print(multiply)

elif variable == "/":
    print(divide)

else:
    print("fel: ogiltig inmatning")


#denna miniräknare är med alla räknesätt inte bara multiplikation
