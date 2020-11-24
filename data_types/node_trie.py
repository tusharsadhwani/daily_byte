"""Standard trie implementation"""
from __future__ import annotations
from typing import Dict, Tuple


class NodeTrie:
    """Represents one character in a trie"""

    def __init__(self, char: str) -> None:
        assert len(char) == 1, (
            'Trie Character should only be initialized with one '
            'character at a time.'
        )
        self.char = char
        self.children: Dict[str, NodeTrie] = {}
        self.is_end = False

    def insert(self, string: str) -> None:
        """Inserts a string into the trie"""
        node, rest = self.search_partial_word(string)
        for char in rest:
            new_node = NodeTrie(char)
            node.children[char] = new_node
            node = new_node
        node.is_end = True

    def search_partial_word(self, string: str) -> Tuple[NodeTrie, str]:
        """Looks for partial words in the trie, and returns last Node"""
        if string == '':
            return (self, string)

        first, rest = string[0], string[1:]
        if first not in self.children:
            return (self, string)

        child = self.children[first]
        return child.search_partial_word(rest)

    def search(self, string: str) -> bool:
        """Inserts a string into the trie"""
        node, _ = self.search_partial_word(string)
        return node.is_end


class TrieRoot(NodeTrie):
    """Root Node of the Trie"""

    def __init__(self) -> None:
        super().__init__('.')
        self.char = ''
        self.children: Dict[str, NodeTrie] = {}
        self.is_end = False
