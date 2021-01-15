"""
You’re running a popsicle stand where each popsicle costs $5. Each
customer you encountered pays with either a $5 bill, a $10 bill, or a
$20 bill and only buys a single popsicle. The customers that come to
your stand come in the order given by the customers array where
customers[i] represents the bill the ith customer pays with. Starting
with $0, return whether or not you can serve all the given customers
while also giving the correct amount of change.

Ex: Given the following customers...

customers = [5, 10], return true
collect $5 from the first customer, pay no change.
collet $10 from the second customer and give back $5 change.

Ex: Given the following customers...

customers = [10], return false
Explanation:
collect $10 from the first customer and we cannot give back change.

Ex: Given the following customers...

customers = [5, 5, 5, 10, 20], return true
Explanation:
collect $5 from the first 3 customers.
collet $10 from the fourth customer and give back $5 change.
collect $20 from the fifth customer and give back $10 change
($10 bill and $5 bill).
"""


def validate_change(customers: list[int]) -> bool:
    """Validates if the cashier can give change to each customer"""
    fives, tens, twenties = 0, 0, 0

    def try_pop(notes: int) -> bool:
        if notes == 0:
            return False

        notes -= 1
        return True

    for cash in customers:
        if cash == 5:
            fives += 1
        elif cash == 10:
            tens += 1
        elif cash == 20:
            twenties += 1

        change = cash - 5

        while change > 0:
            if change >= 20:
                popped = try_pop(twenties)
                if not popped:
                    return False
                change -= 20

            elif change >= 10:
                popped = try_pop(tens)
                if not popped:
                    return False
                change -= 10

            elif change >= 5:
                popped = try_pop(fives)
                if not popped:
                    return False
                change -= 5

            else:
                return False

    return True


def main() -> None:
    """Main function"""
    customers = [5, 10]
    # customers = [10]
    # customers = [5, 5, 5, 10, 20]

    print(validate_change(customers))


if __name__ == "__main__":
    main()
