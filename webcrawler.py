import requests as r
from bs4 import BeautifulSoup as bs
import lxml
from links import Links
from keywords import Keyword


class Webcrawler():
    def __init__(self):
        self.count = 0

    def crawl(self, homepage):
        """ crawls web """

        url = homepage

        rep = r.get(url)

        if rep.status_code == 200:

            soup = bs(rep.text, 'html.parser')

            links = soup.find_all('a')

            for l in links:
                link = (l.get('href'))
                if link:
                    if not link.startswith("http://"):
                        link = url.split('/', 3)[0] + "//" + url.split(
                            '/', 3)[1] + url.split('/', 3)[2] + "/" + link

                    if Links.process_links(link):
                        self.count += 1

                        if self.count > 100:
                            break

                        if url[7:-9] not in link:
                            break
                        self.crawl(link)

    