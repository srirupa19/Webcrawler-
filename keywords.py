import heapq
from stem import stemming
import copy


class Keyword:

    words_dict = {}
    fetched = False

    @classmethod
    def add_keyword(cls, word, link):
        """adds new element to dict of keyword and links"""

        if word in cls.words_dict:
            heapq.heappush(cls.words_dict[word], link)
        else:
            cls.words_dict.setdefault(word, [])
            heapq.heappush(cls.words_dict[word], link)

    @classmethod
    def update(cls, url):
        """updates pagerank and remodifies words_dict order"""
        for word in cls.words_dict:
            for l in cls.words_dict[word]:
                if l.link == url:
                    l.update_pagerank()
    @classmethod
    def give_dict(cls):
        final_dict = {}
        for key in cls.words_dict:

            l = []
            
            while cls.words_dict[key] != []:
                l.append(heapq.heappop(cls.words_dict[key]).link)

            final_dict[key] = l

        return final_dict
