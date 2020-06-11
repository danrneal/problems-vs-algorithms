"""Create a router that can store handlers for paths within a trie.

Usage: request_routing_in_a_web_server_with_a_trie.py

Classes:
    Router()
    RouteTrie()
    RouteTrieNode()
"""

import collections


class Router:
    """Creates a Router class that stores and manipulates a RouteTrie.

    Attributes:
        root_handler: A str representing the handler for the root path
        not_found_handler: A str representing the handler when a given route is
            not found, defaults to None
    """

    def __init__(self, root_handler, not_found_handler=None):
        """Set-up for the router."""
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """Add a handler to the router at a given path.

        Args:
            path: A str representing the path to add the handler at
            handler: A str representing the handler to add
        """
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        """Lookup a handler at a given path.

        Args:
            path: A str representing the path to look for a handler at

        Returns:
            handler: A str representing the handler found at a given path, the
                not_found_handler is returned if no handler is found
        """
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)
        if handler is None:
            handler = self.not_found_handler

        return handler

    @staticmethod
    def split_path(path):
        """Splits a path str into its parts.

        Args:
            path: A str representing the path to split

        Returns:
            path_parts: A list of strs that represent the parts of the path
                split on slashes, strips trailing slashes
        """
        path = path.rstrip("/")
        path_parts = path.split("/")[1:]

        return path_parts


class RouteTrie:
    """Creates a RouteTrie object containing routes and associated handlers.

    Attributes:
        root: A RouteTrieNode object that represents the root node of the trie
    """

    def __init__(self, root_handler):
        """Set-up for the route trie."""
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
        """Add a route and associated handler into the route trie.

        Args:
            path_parts: A list of strs representing the parts of the path to
                add to the trie
            handler: A str representing the handler to add at the end of the
                given path
        """
        node = self.root
        for part in path_parts:
            node = node.children[part]

        node.handler = handler

    def find(self, path_parts):
        """Find the handler at the node that represents a given path.

        Args:
            path_parts: A list of strs that represents the parts of the path to
                search for the handler at

        Returns: A str representing the handler at the node located at the
            given path, returns None if not found
        """
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None

            node = node.children[part]

        return node.handler


class RouteTrieNode:
    """Creates a RouteTrieNode object to store a path in a RouteTrie.

    Attributes:
        children: A defaultdict object that creates a dictionary with a default
            value of a RouteTrieNode object
        handler: A str representing the handler stored at the path that this
            node represents, defaults to None
    """

    def __init__(self, handler=None):
        """Set-up for the route trie node."""
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = handler


def main():
    """Main function call to test the overall router implementation."""
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    assert router.lookup("/") == "root handler"
    assert router.lookup("/home") == "not found handler"
    assert router.lookup("/home/about") == "about handler"
    assert router.lookup("/home/about/") == "about handler"
    assert router.lookup("/home/about/me") == "not found handler"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
