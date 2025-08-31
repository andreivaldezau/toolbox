from typing import Any, List


class HashTable:
    def __init__(self) -> None:
        self.capacity = 16
        self.load_factor = 0.8
        self.buckets: List[Any] = []
