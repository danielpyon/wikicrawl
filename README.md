# wikicrawl

## how it works

The code crawls through a Wikipedia page by breadth-first-search, measuring page popularity (by # of links) along the way. Max crawl depth is 2. It writes the output to a file, ranking related sites from lowest to highest popularity.

## results

The starting page was [NOP Slide](https://en.wikipedia.org/wiki/NOP_slide), a technique in computer security for exploiting a binary.

The most popular related page was "U.S." (5556 links), followed by "Evolution" (5440 links), and "European_Union" (4395 links). The most popular topic related to security was "National_Security_Agency" (3826 links), and the most popular one related to binary exploitation specifically was "ARM_architecture" (2512 links). The topics are not all technology/computer related, which I thought was surprising, especially with a mere depth 2 crawler.

It's interesting to think about the balance between popularity and relevance. Past a certain cutoff point (in this case, maybe 500 links), the topics seem to become too broad. Topics with around 500 links and under appear to be okay (as in, related to the original topic of NOP slides), but above that, there's a lot of irrelevant stuff. For instance, "U.S." is clearly unrelated to the original topic.

It was also interesting to observe the output of the program when running a BFS versus a DFS. With a BFS, topics processed near each other (aka topics visited by the crawler in succession) had no clear pattern, whereas with a DFS, topics explored in succession were often directly to each other (for example, "Assembly Language" might lead to "x86").

