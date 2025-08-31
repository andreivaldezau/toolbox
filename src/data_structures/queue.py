from collections import deque
from typing import Any


class Queue:
    """Class of a queue."""

    def __init__(self) -> None:
        """Generate a queue using collections deque method. This uses a doubly linked list."""
        self.data = deque()

    def enqueue(self, node: Any) -> None:
        """Enqueue an item to the queue.

        Args:
            node (Any): item to be added
        """
        self.data.append(node)

    def dequeue(self):
        """Dequeue an item from the queue."""
        self.data.popleft()
