menu={
    "Pizza": 500,
    "Burger": 300,
    "Pasta": 400,
    "Coke": 100,
    "French Fries": 200,
    "Sandwich": 150
}

print("Welcome to the PYTHON Restaurant")
print("Menu:\nPizza:Rs500\nBurger:Rs300\nPasta:Rs400\nCoke:Rs100\nFrench Fries:Rs200\nSandwich:Rs150")
total = 0
ordered_items = input("Enter the items you want to order: ").split(",")
for item in ordered_items:
    item = item.strip()  # Remove leading/trailing whitespace
    if item in menu:
        total += menu[item]
        print(f"You ordered {item} and your total bill is {total}")
    else:
        print(f"Invalid item: {item}")

while True:
    more_items = input("Do you want to order something else? (Yes/No) ")
    if more_items.lower() == "yes":
        ordered_items = input("Enter the items you want to order: ").split(",")
        for item in ordered_items:
            item = item.strip()  # Remove leading/trailing whitespace
            if item in menu:
                total += menu[item]
                print(f"You ordered {item} and your total bill is {total}")
            else:
                print(f"Invalid item: {item}")
    else:
        break