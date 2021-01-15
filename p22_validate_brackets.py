"""
Given a string only containing the following characters:
    (, ), {, }, [, and ],

return whether or not the opening and closing characters are in a valid
order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
"""


def validate_brackets(brackets: str) -> bool:
    """Validate the sequence of given brackets"""
    stack: list[str] = []

    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    valid_brackets = [bracket for pair in pairs.items() for bracket in pair]

    for bracket in brackets:
        if bracket not in valid_brackets:
            raise ValueError('Invalid input')

        if bracket in pairs:
            # All opening brackets to be pushed to stack
            stack.append(bracket)
        else:
            # Closing bracket found, checking if pop possible
            if len(stack) == 0:
                return False

            top_bracket = stack[-1]
            if bracket != pairs[top_bracket]:
                # Invalid bracket pair
                return False

            # Valid bracket pair found, remove from stack
            stack.pop()

    # Stack should be empty in the end
    return len(stack) == 0


def main() -> None:
    """Main function"""
    brackets = input('> ')
    print(validate_brackets(brackets))


if __name__ == "__main__":
    main()
