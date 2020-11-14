"""
You are serving people in a lunch line and need to ensure each person
gets a “balanced” meal. A balanced meal is a meal where there exists the
same number of food items as drink items. Someone is helping you prepare
the meals and hands you food items (i.e. F) or a drink items (D) in the
order specified by the items string.

Return the maximum number of balanced meals you are able to create
without being able to modify items.

Note: items will only contain F and D characters.

Ex: Given the following items...

items = "FDFDFD", return 3
the first "FD" creates the first balanced meal.
the second "FD" creates the second balanced meal.
the third "FD" creates the third balanced meal.

Ex: Given the following items...

items = "FDFFDFDD", return 2
"FD" creates the first balanced meal.
"FFDFDD" creates the second balanced meal.
"""


def main() -> None:
    """Main function"""
    meals = 0

    items = input('> ')
    foods, drinks = 0, 0
    for item in items:
        if item == 'F':
            foods += 1
        elif item == 'D':
            drinks += 1

        if foods == drinks:
            meals += 1
            foods, drinks = 0, 0

    print(meals)


if __name__ == "__main__":
    main()
