cook_times = {
    "small": 30,
    "medium": 60,
    "large": 75,
    "xlarge": 135
}

Small = int(input(f"Enter the number of small sandwiches: "))
Medium = int(input(f"Enter the number of medium sandwiches: "))
Large = int(input(f"Enter the number of large sandwiches: "))
XLarge = int(input(f"Enter the number of extra-large sandwiches: "))

print()

print(f"You've entered {Small} small sandwiches.")
print(f"You've entered {Medium} medium sandwiches.")
print(f"You've entered {Large} large sandwiches.")
print(f"You've entered {XLarge} extra-large sandwiches.")

print()

Total_Cook = (Small * cook_times['small'] +
              Medium * cook_times['medium'] +
              Large * cook_times['large'] +
              XLarge * cook_times['xlarge'])

mins = int(Total_Cook // 60)
secs = int(Total_Cook % 60)

print(f"Total cooking time is {mins} minutes and {secs} seconds.")
