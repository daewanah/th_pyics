try:
    count = int(input("You want some HIs? Tell me how much you want: "))
except ValueError:
    print("That's not a number!")
else:
    print("Hi " * count)
