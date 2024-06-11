class Stack:
    """Class of a stack."""

    def __init__(self) -> None:
        """Generate a stack."""
        self.data: list = []

    def push(self, node: any) -> None:
        """Insert an item to the end of the stack.

        Args:
            node (any): item to be added
        """
        self.data.append(node)

    def pop(self) -> any:
        """Remove the last item from the stack."""
        return self.data.pop()
