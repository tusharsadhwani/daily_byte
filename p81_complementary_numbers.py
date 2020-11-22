"""
Given a positive number, return its complementary number.
Note: The complement of a number is the number that results from
flipping every bit in the original number. (i.e. zero bits become one
bits and one bits become zero bits).

Ex: Given the following number…

number = 27, return 4.
27 in binary (not zero extended) is 11011.
Therefore, the complementary binary is 00100 which is 4.
"""


def main() -> None:
    """Main function"""
    number = int(input('> '))

    binary = f'{number:b}'
    complement = ''.join('0' if bit == '1' else '1' for bit in binary)
    complement_int = int(complement, 2)
    print(complement_int)

    # # Alternative approach:
    # binary = f'{number:b}'
    # print(~number + 2 ** len(binary))


if __name__ == "__main__":
    main()
