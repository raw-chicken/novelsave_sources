from dataclasses import dataclass, field
from typing import List, Optional

from .metadata import Metadata
from .volume import Volume


@dataclass
class Novel:
    title: str
    url: str
    author: Optional[str] = None
    synopsis: List[str] = field(default_factory=lambda: [])
    thumbnail_url: Optional[str] = None
    status: Optional[str] = None
    lang: str = "en"

    volumes: List[Volume] = field(default_factory=lambda: [])
    metadata: List[Metadata] = field(default_factory=lambda: [])

    def get_default_volume(self):
        if self.volumes:
            return self.volumes[0]

        volume = Volume.default()
        self.volumes.append(volume)
        return volume

    def add_metadata(self, *args, **kwargs):
        self.metadata.append(Metadata(*args, **kwargs))
