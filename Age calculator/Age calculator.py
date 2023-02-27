# --------------------
# -- Age calculator --
# --------------------

while True:

    age = int(input("Please enter your age: "))

    months = age * 12
    weeks = months * 4
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print("----------------------------")
    print(f"You are {age} years old.")
    print("----------------------------")
    print('You Lived For:')
    print(f"- {months} Months.")
    print(f"- {weeks:,} Weeks.")
    print(f"- {days:,} Days.")
    print(f"- {hours:,} Hours.")
    print(f"- {minutes:,} Minutes.")
    print(f"- {seconds:,} Seconds.")
    print("----------------------------")
    print()
    print("Do you want to calculate another age?")
    print("- Yes [1]")
    print("- No [2]")
    a = input("Select > ")
    if a == "1":
        print("----------------------------")
    else:
        break
