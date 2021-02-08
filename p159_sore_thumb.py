"""
Students in a class are lining up in ascending height order, but are
having some trouble doing so. Because of this, it’s possible that some
students might be out of order. In particular, a student that is taller
than both their neighboring students (i.e. the person to both their left
and right) sticks out like a sore thumb. Given an integer array that
represents each students height, return the index of a “sore thumb”.

Note: If there are multiple sore thumbs you may return the index of any
of them. All numbers in the array will be unique.

Ex: Given the following students...

students = [1, 2, 3, 7, 5], return 3.
"""


def sore_thumb(students: list[int]) -> int:
    """Returns index of sore thumb"""
    last_height = students[0]
    for index, height in enumerate(students[1:], start=1):
        if last_height > height:
            return index - 1

        last_height = height

    return -1


def main() -> None:
    """Main function"""
    students = [1, 2, 3, 7, 5]
    print(sore_thumb(students))


if __name__ == '__main__':
    main()
