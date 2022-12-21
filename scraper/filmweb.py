from requests_html import HTML, HTMLSession
from datetime import datetime, timedelta
from urllib.parse import unquote_plus
from .links import Link, CollectedLinks, CollectedTitles
from .data import CollectedData
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import re

@dataclass
class GetData (ABC):

    url: str = field(default='')
    params: dict = field(default_factory=dict)

    def establish_session (self):
        session = HTMLSession()
        self.r = session.get(self.url, params=self.params)
        return self

    @abstractmethod
    def get_data (self, page) -> CollectedData:
        pass


# prepare class for every type of data?????

class GetLinks (GetData):
    """
    selector_links - CSS selector of tag where is link to full description

    selectro_title - CSS selector of origninal tittle
    """

    selector_link: str = 'div > div > div.preview__card > div.preview__header > h2 > a'
    selector_title: str = 'div.preview__header > div.preview__headerDetails > div.preview__alternateTitle'
    selector_person: str = 'div > div.hit__desc > div.hit__name > h3 > a'


    def parse_year(self, link: str) -> int:
        pattern = '.*-(\d{4})-\d*'
        return int(re.findall(pattern, link)[0])

    def parse_id(self, link: str) -> int:
        pattern = '.*-\d{4}-(\d*)'
        return int(re.findall(pattern, link)[0])

    # change name of method to get_movie_links

    # better solution will be if you prepare dofferent methods for different tasks
    def get_data(self, page: int) -> CollectedData:

        self.params['page'] = str(page)
        self.establish_session()
        if self.r.status_code != 200:
            return None
        links = self.r.html.find(self.selector_link)
        collection_links = CollectedLinks()

        for link in links:
            linkHTML = link.attrs['href']
            titleUTF8 = link.text
            year = self.parse_year(linkHTML)
            ID = self.parse_id(linkHTML)
            collection_links.add_link(Link(linkHTML, titleUTF8, year, ID))

        return collection_links
            

            
        