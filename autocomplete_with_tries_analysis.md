# Autocomplete with Tries

## Design Choices

For the TrieNode I initialized the children property using the defaultdict import form the collections library to store children as new TrieNodes. I also had a TrieNode have the method of finding all the suffixes below it. The insert method of the Trie will insert new nodes into the Trie with a TrieNode for each character in an inserted word. The find method simply finds the node for the given prefix where suffixes can then be accessed.

## Time Complexity

Lookup for a given trie involves the find method of the Trie and the suffixes method on the TrieNode. The find method will happen in O(n) time since it must traverse a single route on the trie according the the characters of the prefix. The suffixes method is a bit more complex since it must traverse the entire tree below that point along every path. The complexity does not depend on the size of the prefix then but on the size of the trie. This will have a time complexity of O(m\*l) where m is the number of words in the trie and l is the length of the longest word. This will be the dominant factor and thus the time complexity to the autocomplete function is O(m\*l)

## Space Complexity

The space complexity for the trie will be the proportional to the number of nodes which will depend on the size of the trie which as discussed in the previous section will be O(m\*l).
