"""Program that takes two binary numbers as input and outputs their sum"""
from itertools import zip_longest


def half_adder(bit_a: str, bit_b: str) -> (str, str):
    """Half adder implementation"""
    carry = bit_b if bit_a == '1' else '0'
    _sum = bit_b if bit_a == '0' else '1' if bit_b == '0' else '0'
    return carry, _sum


def full_adder(bit_a: str, bit_b: str, bit_c: str) -> (str, str):
    """Full adder implementation using half adders"""
    carry1, sum1 = half_adder(bit_a, bit_b)
    carry2, _sum = half_adder(sum1, bit_c)
    carry = carry2 if carry1 == '0'else '1'
    return carry, _sum


def main():
    """Main function"""
    num1 = input('> ')[::-1]
    num2 = input('> ')[::-1]

    carry = '0'
    ans = ''
    for bit_a, bit_b in zip_longest(num1, num2, fillvalue='0'):
        carry, bit = full_adder(bit_a, bit_b, carry)
        ans += bit
    if carry == '1':
        ans += carry
    print('Sum:', ans[::-1])


if __name__ == "__main__":
    main()
