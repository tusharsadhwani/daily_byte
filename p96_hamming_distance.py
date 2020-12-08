"""
Given two integers x and y, return the hamming distance between the two
numbers.

Note: The hamming distance between two numbers is the number of bit
positions in which the bits differ.

Ex: Given the following integers x and y...

x = 2, y = 4, return 2.
2 in binary is 0 0 1 0
4 in binary is 0 1 0 0
therefore the number of positions in which the bits differ is two.
"""


def main() -> None:
    """Main function"""
    num1, num2 = 2, 4
    # num1, num2 = 54, 9

    num1_binary = f'{num1:b}'
    num2_binary = f'{num2:b}'

    length = max((len(num1_binary), len(num2_binary)))

    num1_binary = f'{num1_binary:0>{length}}'
    num2_binary = f'{num2_binary:0>{length}}'

    count = 0
    for bit1, bit2 in zip(num1_binary, num2_binary):
        if bit1 != bit2:
            count += 1

    print(count)


def alternative() -> None:
    num1, num2 = 2, 4
    # num1, num2 = 54, 9

    xor = num1 ^ num2

    # TODO: py3.10 has a int.bit_count() function which can replace this
    print(bin(xor).count('1'))


if __name__ == "__main__":
    main()
    alternative()
