from typing import Any


class Stack:
    """Class of a stack."""

    def __init__(self) -> None:
        """Generate a stack."""
        self.data: list = []

    def push(self, node: Any) -> None:
        """Insert an item to the end of the stack.

        Args:
            node (Any): item to be added
        """
        self.data.append(node)

    def pop(self):
        """Remove the last item from the stack."""
        self.data.pop()
