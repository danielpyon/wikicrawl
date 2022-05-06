from bs4 import BeautifulSoup, SoupStrainer
from requests import get
from re import compile, match
from collections import deque

if __name__ == '__main__':
    START_PAGE = 'https://en.wikipedia.org/wiki/Free_software'

    # Links should start with "/wiki/" and must exclude special Wikipedia pages
    pattern = compile('^/wiki/[^(File:)(Wikipedia:)(Portal:)(Help:)(Special:)(Talk:)(Category:)]')

    visited = set()
    visited.add(START_PAGE)

    to_visit = deque()
    to_visit.append(START_PAGE)

    while len(to_visit) > 0:
        site = to_visit.popleft()
        soup = BeautifulSoup(get(site).text, 'html.parser')
        for link in soup.find_all('a', href=True):
            url = 'https://en.wikipedia.org' + link['href']
            if url not in visited and pattern.match(url):
                visited.add(url)
                to_visit.append(url)
    
    print(visited)
