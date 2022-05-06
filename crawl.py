from bs4 import BeautifulSoup, SoupStrainer
from requests import get
from re import compile, match
from collections import deque

if __name__ == '__main__':
    START_PAGE = 'https://en.wikipedia.org/wiki/Siteswap'

    # Links should start with "/wiki/" and must exclude special Wikipedia pages
    # Note that Main_Page is excluded (it has no relation to the current page)
    pattern = compile('^/wiki/[^(File:)(Wikipedia:)(Portal:)(Help:)(Special:)(Talk:)(Category:)(Main_Page)]')

    visited = set()
    visited.add(START_PAGE)

    # All URLs in the queue are a tuple: (url, depth)
    to_visit = deque()
    to_visit.append((START_PAGE, 0))

    # (url, popularity measured in links)
    popularity = list()

    while len(to_visit) > 0:
        parent_url, parent_depth = to_visit.pop()
        html = get(parent_url).text
        soup = BeautifulSoup(html, 'html.parser')

        print(f'Processing {parent_url}, which has depth {parent_depth}')

        links = soup.find_all('a', href=True)
        
        if parent_depth <= 2:
            popularity.append((parent_url, len(links)))
        if parent_depth == 2:
            # Don't add children
            continue

        for link in links:
            child_url = 'https://en.wikipedia.org' + link['href']
            child_depth = parent_depth + 1

            if child_url not in visited and pattern.match(link['href']) and child_depth <= 2:
                visited.add(child_url)

                # The child depth is the parent depth + 1
                to_visit.append((child_url, child_depth))
    
    popularity = sorted(popularity, lambda x: x[1])
    print(popularity)
