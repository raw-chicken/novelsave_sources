from dataclasses import dataclass

from typing import Tuple


@dataclass
class Chapter:
    index: int = -1
    no: float = None
    title: str = None
    paragraphs: str = None
    volume: Tuple[int, str] = None
    url: str = None

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        return self.url == other.url
