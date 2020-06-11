"""Create a dictionary that can autocomplete words given a prefix.

Usage: autocomplete_with_tries.py

Classes:
    Trie()
    TrieNode()
"""

import collections


class Trie:
    """Creates a Trie object that serves as the dictionary.

    Attributes:
        root: A TrieNode object that represents the root node of the trie
    """

    def __init__(self):
        """Set-up for the trie."""
        self.root = TrieNode()

    def insert(self, word):
        """Add a word into the trie.

        Args:
            word: A str to add into the trie
        """
        node = self.root
        for char in word:
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        """Find the node that represents a given prefix.

        Args:
            prefix: A str that represents the prefix of the node to search for

        Returns: A TrieNode object that represents the node that represents the
            given prefix, returns None if not found
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None

            node = node.children[char]

        return node


class TrieNode:
    """Creates a TrieNode object to store information in a Trie.

    Attributes:
        children: A defaultdict object that creates a dictionary with a default
            value of a TrieNode object
        is_word: A bool representing if this node is a terminal node of a word
    """

    def __init__(self):
        """Set-up for the trie node."""
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def suffixes(self, suffix=""):
        """Retrieves suffixes for all complete words in this node's children.

        Args:
            suffix: A str representing the previous chars traversed provided to
                each child node, default is the empty string

        Returns:
            words: A list of strs representing the suffixes to all complete
                words contained in this node's children
        """
        words = []
        for char in self.children:
            words += self.children[char].suffixes(suffix=suffix + char)
            if self.children[char].is_word:
                words.append(suffix + char)

        return words


def main():
    """Main function call to test autocomplete trie implementation."""
    my_trie = Trie()
    word_list = [
        "ant",
        "anthology",
        "antagonist",
        "antonym",
        "fun",
        "function",
        "factory",
        "trie",
        "trigger",
        "trigonometry",
        "tripod",
    ]

    for word in word_list:
        my_trie.insert(word)

    prefix = input("Please enter a prefix: ")
    autocomplete(prefix, my_trie)


def autocomplete(prefix, trie):
    """Print all possible suffixes in a trie from a given prefix.

    Args:
        prefix: A str representing the prefix to the words to search for
        trie: A Trie object representing the dictionary to look in
    """
    prefix_node = trie.find(prefix)
    if prefix_node is not None:
        print("Possible suffixes:")
        print("\n".join(prefix_node.suffixes()))
    else:
        print(prefix + " not found")


if __name__ == "__main__":
    main()
