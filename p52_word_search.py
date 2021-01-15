"""
Given a 2D board that represents a word search puzzle and a string word,
return whether or the given word can be formed in the puzzle by only
connecting cells horizontally and vertically.

Ex: Given the following board and words...

board = [
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
word = "CAT", return true
word = "TEA", return true
word = "SEAT", return true
word = "BAT", return false
"""


def get_valid_adjacent_coords(
        board: list[list[str]],
        coords: tuple[int, int],
        char: str) -> list[tuple[int, int]]:
    """Gets all valid adjacent coordinates matching the given char"""
    # NOTE: Currently this function doesn't keep track of already used
    # indices, assuming using the same characters repeatedly is allowed.

    x_coord, y_coord = coords
    indices: list[tuple[int, int]] = []

    for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        new_x, new_y = x_coord+i, y_coord+j

        if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
            if board[new_x][new_y] == char:
                indices.append((new_x, new_y))

    return indices


def find_word_chunk(
        board: list[list[str]],
        coords: tuple[int, int],
        chunk: str) -> bool:
    """
    Recursive algorithm to find a word chunk adjacent to the given
    coordinates in the 2D word board.
    """
    if chunk == '':
        return True

    char, rest = chunk[0], chunk[1:]
    adjacent_coords = get_valid_adjacent_coords(board, coords, char)

    return any(find_word_chunk(board, coords, rest)
               for coords in adjacent_coords)


def find_word(word: str, board: list[list[str]]) -> bool:
    """Returns if the given word can be found in the 2D word board."""
    word = word.upper()

    head, rest = word[0], word[1:]
    indices = [(x, y)
               for x, row in enumerate(board)
               for y, char in enumerate(row)
               if char == head]

    for coords in indices:
        found = find_word_chunk(board, coords, rest)
        if found:
            return True

    return False


def main() -> None:
    """Main function"""
    board = [
        ['C', 'A', 'T', 'F'],
        ['B', 'G', 'E', 'S'],
        ['I', 'T', 'A', 'E']
    ]
    word = input('> ')

    found = find_word(word, board)
    print(found)


if __name__ == "__main__":
    main()
