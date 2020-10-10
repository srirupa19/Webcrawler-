import requests as r
from bs4 import BeautifulSoup as bs
from keywords import Keyword
from stem import stemming


class Link():
    def __init__(self, link):
        self.link = link
        self.pagerank = -1

    def __hash__(self):
        return hash(self.link)

    def __eq__(self, other):
        return (self.link) == (other.link)

    def __lt__(self, other):
        return (self.pagerank) < (other.pagerank)

    def __gt__(self, other):
        return (self.pagerank) > (other.pagerank)

    def keywords(self):
        """ returns keywords from page """

        url = self.link
        rep = r.get(url)

        text = ""

        if rep.status_code == 200:
            soup = bs(rep.text, 'html.parser')
            text = soup.get_text()

        word_set = stemming(text)

        for word in word_set:

            Keyword.add_keyword(word, self)

    def update_pagerank(self):
        """ updates pagerank """
        self.pagerank -= 1
