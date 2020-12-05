"""
Given a valid IP address, defang it.
Note: To defang an IP address, replace every ”.”, with ”[.]”.

Ex: Given the following address...

address = "127.0.0.1", return "127[.]0[.]0[.]1"
"""


def main() -> None:
    """Main function"""
    address = input('> ')
    print(address.replace('.', '[.]'))


if __name__ == "__main__":
    main()
