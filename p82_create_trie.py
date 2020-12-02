"""
Create a trie class that supports insertion and search functionalities.

Note: You may assume only lowercase alphabetical characters will added
to your trie.

Ex: Given the following operations on your trie...

Trie trie = new Trie()
trie.insert("programming");
trie.search("computer") // returns false.
trie.search("programming") // returns true.
"""


from data_types.node_trie import TrieRoot


def main() -> None:
    """Main function"""
    trie = TrieRoot()

    trie.insert("programming")
    print(trie.search("computer"))
    print(trie.search("programming"))


if __name__ == "__main__":
    main()
