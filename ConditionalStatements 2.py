num_1 = input("please enter your first number: ")
num_2 = input("please enter your second number: ")
operations = ["+", "-", "*", "/", "^", "%"]
result = 0

print(operations)

operat = input("please choose one of the previous operations: ")

if operat == "+" or operat == "1":
    result = int(num_1) + int(num_2)
    print(result)
elif operat == "-" or operat == "2":
    result = int(num_1) - int(num_2)
    print(result)
elif operat == "*" or operat == "3":
    result = int(num_1) * int(num_2)
    print(result)
elif operat == "/" or operat == "4":
    result = int(num_1) / int(num_2)
    print(result)
elif operat == "^" or operat == "5":
    result = int(num_1) ** int(num_2)
    print(result)
elif operat == "%" or operat == "6":
    result = int(num_1) % int(num_2)
    print(result)
