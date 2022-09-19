

print("Hello Friend")


name = input("input your name: ")
age = input("input your age: ")
address = input("input your address: ")
if name.isalpha() == True:
    if age.isdigit() == True:
        print(
            f"Hello Mr\Ms {name} age is {age} and located in {address} thanks for being one of our coomuunity")
    else:
        print("please enter a number of age")
else:
    print("please enter a name not a number")
