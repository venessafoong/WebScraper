# Script that asks for user's filters in the terminal

def get_listingtype():
    while True:
        print("Are you buying or renting?")
        while True:
            listing = input("buy/rent: ")
            if listing.lower() == "buy":
                break
            elif listing.lower() == "rent":
                break
            else:
                print("Please input a valid answer.")
        print(f"You are looking to {listing.lower()}.")
        if confirmation():
            return listing

def get_bedrooms():
    while True:
        print("\nHow many bedrooms?(Type )")
        rooms_arr = []
        while True:
            try:
                rooms = int(input("Please enter an integer(0-5) or (9) once you are done: "))
                if rooms == 9:
                    break
                elif 0 < rooms < 6:
                    rooms_arr.append(rooms)
                else:
                    print("Please input a valid integer.")
            except ValueError:
                print("Please input a valid integer.")
        print(f"You are looking at houses with {rooms_arr} bedrooms.")
        if confirmation():
            return rooms_arr

def get_budget():
    while True:
        print("\nWhat is your budget?")
        while True:
            try:
                min = int(input("Please enter the minimum price: "))
                break
            except ValueError:
                print("Please input a valid integer.")
        while True:
            try:
                max = int(input("Please enter the maximum price: "))
                break
            except ValueError:
                print("Please input a valid integer.")
        print(f"Your budget is from ${min} to ${max}.")
        if confirmation():
            return (min, max)

def confirmation() -> bool:
    while True:
        confirm = input("y/n: ")
        if confirm in ["Y","y"]:
            return True
        elif confirm in ["N","n"]:
            return False
        else:
             print("Please input a valid character.")

print("\n~~ Find your perfect property ~~")
print("\nFirst we need to ask you some questions.")
listing = get_listingtype()
bedrooms = get_bedrooms()
min_price, max_price = get_budget()