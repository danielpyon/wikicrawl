from bs4 import BeautifulSoup, SoupStrainer
from requests import get
from re import compile, match
from collections import deque

if __name__ == '__main__':
    START_PAGE = 'https://en.wikipedia.org/wiki/Siteswap'

    # Links should start with "/wiki/" and must exclude special Wikipedia pages
    pattern = compile('^/wiki/[^(File:)(Wikipedia:)(Portal:)(Help:)(Special:)(Talk:)(Category:)]')

    visited = set()
    visited.add(START_PAGE)

    # All URLs in the queue are a tuple: (url, depth)
    to_visit = deque()
    to_visit.append((START_PAGE, 0))

    # (url, popularity measured in links)
    popularity = list()

    while len(to_visit) > 0:
        parent_url, parent_depth = to_visit.popleft()
        html = get(parent_url).text
        soup = BeautifulSoup(html, 'html.parser')

        links = soup.find_all('a', href=True)
        popularity.append((parent_url, len(links)))
        
        for link in links:
            child_url = 'https://en.wikipedia.org' + link['href']
            child_depth = parent_depth + 1

            if child_url not in visited and pattern.match(link['href']) and child_depth <= 2:
                visited.add(child_url)

                # The child depth is the parent depth + 1
                to_visit.append((child_url, child_depth))
    
    popularity = sorted(popularity, lambda x: x[1])
    print(popularity)
