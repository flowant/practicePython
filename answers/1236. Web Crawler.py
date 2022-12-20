# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        """
        1236. Web Crawler

        BFS

        """

        def _get_domain(url):
            index = len(url)
            for i in range(7, len(url)):
                if url[i] == '/':
                    index = i
                    break
            return url[7:index]

        domain = _get_domain(startUrl)
        visited = set([startUrl])
        dq = deque([startUrl])

        while dq:
            url = dq.pop()
            for next_url in htmlParser.getUrls(url):
                if domain == _get_domain(next_url) and next_url not in visited:
                    dq.appendleft(next_url)
                    visited.add(next_url)

        return list(visited)
