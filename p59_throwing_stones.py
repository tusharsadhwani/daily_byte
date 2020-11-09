"""
You are given a group of stones, all of which have a positive weight.
At each turn, we select the heaviest two stones and smash them together.
When smashing these two stones together, one of two things can happen:

- If the stones are both the same weight, both stones are destroyed
- If the weights of the stones are not equal, the smaller of the two
  stones is destroyed and the remaining stone’s weight is updated to the
  difference (i.e. if we smash two stones together of weight 3 and
  weight 5 the stone with weight 3 is destroyed and the stone with
  original weight 5 now has weight 2).

Continue smashing stones together until there is at most one stone left
and return weight of the remaining stone. If no stones remain return 0.

Ex: Given the following stones…

stones = [2, 4, 3, 8], return 1
Explanation:
8 and 4 are smashed together, 4 is destroyed, 8 becomes 4.
4 and 3 are smashed together, 3 is destroyed, 4 becomes 1.
2 and 1 are smashed together, 1 is destroyed, 2 becomes 1.
1 is the last stone remaining and is therefore returned.

Ex: Given the following stones…

stones = [1, 2, 3, 4], return 0
Explanation:
4 and 3 are smashed together, 3 is destroyed, 4 becomes 1.
2 and 1 are smashed together, 1 is destroyed, 2 becomes 1.
1 and 1 are smashed together and both stones are destroyed.
0 is returned as no stones remain.
"""
from typing import List


def smash_stones(stones: List[int]) -> int:
    """Smashes stones together until one value remains"""
    stones.sort()

    while len(stones) >= 2:
        stone1 = stones.pop()
        stone2 = stones.pop()

        difference = abs(stone1 - stone2)
        if difference > 0:
            stones.append(difference)

    if not stones:
        return 0

    return stones[0]


def main() -> None:
    """Main function"""
    stones = [2, 4, 3, 8]
    # stones = [1, 2, 3, 4]

    print(smash_stones(stones))


if __name__ == "__main__":
    main()
