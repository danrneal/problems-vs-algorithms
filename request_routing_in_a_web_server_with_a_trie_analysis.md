# Request Routing in a Web Server with a Trie

## Design Choices

The Router will contain the RouteTrie consisting of RouteNodes. The Router will have the ability to add_handlers and to lookup a handler at a given path. The split path can break a path into its requisite parts after stripping off any trailing slashes. If a handler is not found at a given path, the not_found_handler is given (which itself defaults to None).

## Time Complexity

The time complexity of looking up a handler at a given path will involve first splitting the path which will happen O(n) time. Then it must traverse the trie along each part of the path which will also happen in O(n) time. And lastly, it will need to lookup the handler (or lack thereof) at the resulting node which happens in constant O(1) time. Therefore the dominating time complexity of lookup is O(n).

## Space Complexity

The space complexity of the trie has to do with how many paths it holds and how long the paths are. The total space complexity of the Router will be O(n\*m) where n is the number of paths and m is the length.
