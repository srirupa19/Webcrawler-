import webcrawler as web
from stem import stemming
from textname import name
import sqlite3


class Results:

    def __init__(self , homepage):
        self.homepage = homepage

    def crawlnow(self):
        """ asks webcrawler to crawl if site not visited """
        w = web.Webcrawler()
        w.crawl(self.homepage)
        pagebook = web.Keyword.give_dict()

        # file 
        file = name(self.homepage)
        with open(file + ".txt", "w", encoding="utf-8") as f:
            f.write(str(pagebook))



    def fetch(self , words):
        """ fetches results """
        file = name(self.homepage)
        with open(file + ".txt", "r", encoding="utf-8") as f:
            words_dict = eval(f.read())

        keys = stemming(words)
        links = []

        for key in keys:

            if key in words_dict:
                links.append(words_dict[key])

        if links:
            results = links[0]
        else:
            results = []

        for link in links:

            results = [x for x in results if x in link]

        return results