print(f"Welcome!")
num = float(input(f"Please input a number: "))

print()

print(f"What would you like to do with this number:")
print(f"0) Get the additive inverse of the number")
print(f"1) Get the reciprocal of the number")
print(f"2) Square the number")
print(f"3) Cube the number")
print(f"4) Exit the program")
op = int(input())

if op == 0:
    print(f"The additive inverse of {num} is {-num}")
elif op == 1:
    if num == 0:
        print(f"Cannot divide by 0!")
    else:
        print(f"The reciprocal of {num} is", round(num ** -1, 3))
elif op == 2:
    print(f"The square of {num} is", (num ** 2))
elif op == 3:
    print(f"The cube of {num} is", (num ** 3))
elif op == 4:
    print(f"Thank you, goodbye!")
else:
    print(f"Invalid option!")
