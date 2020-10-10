from link import Link
from keywords import Keyword


class Links():

    links_dict = dict()

    @classmethod
    def process_links(cls, link):
        """ checks if present in list or/and updates pagerank"""

        new_link = Link(link)

        if new_link.link not in cls.links_dict:
            cls.links_dict[new_link.link] = new_link
            new_link.keywords()
            return True
        else:
            cls.links_dict[new_link.link].update_pagerank()
            Keyword.update(link)
            return False
