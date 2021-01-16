"""
High school students are voting for their class president and you’re
tasked with counting the votes. Each presidential candidates is
represented by a unique integer and the candidate that should win the
election is the candidate that has received more than half the votes.
Given a list of integers, return the candidate that should become the
class president.

Note: You may assume there is always a candidate that has received more
than half the votes.

Ex: Given the following votes...

votes = [1, 1, 2, 2, 1], return 1.
Ex: Given the following votes...

votes = [1, 3, 2, 3, 1, 2, 3, 3, 3], return 3.
"""


def majority_element(nums: list[int]) -> int:
    """Returns the element that appears more than N/2 times in a list"""
    candidate = nums[0]
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


def main() -> None:
    """Main function"""
    votes = [1, 1, 2, 2, 1]
    # votes = [1, 3, 2, 3, 1, 2, 3, 3, 3]

    print(majority_element(votes))


if __name__ == "__main__":
    main()
