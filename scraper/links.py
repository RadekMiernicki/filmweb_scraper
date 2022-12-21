from dataclasses import dataclass, field
from .data import CollectedData

@dataclass
class Link:

    linkHTML: str
    titleUTF8: str
    year: int
    filmwebID: int

# prepare class for every type of data which you like to collect

@dataclass
class CollectedLinks(CollectedData):

    links: list[Link] = field(default_factory=list)

    def add_link(self, link: Link) -> None:
        self.links.append(link)

    def retrive_data(self) -> list[Link]:
        return self.links

@dataclass
class CollectedTitles(CollectedData):

    titles: list[str] = field(default_factory=list)

    def add_title(self, title: str) -> None:
        self.titles.append(title)

    def retrive_data(self) -> list[str]:
        return self.titles