import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

def get_url(filter, web_url ,soup=None):
    # This function parse the html given by soup(A Beautiful Soup object). If not given, it request one from web_url
    # It need a filter(Actually it's a regex expression) to filter the href in the html 
    # It returns the url we get from html
    if not soup:
        r = requests.get(web_url)
        soup = BeautifulSoup(r.content,features="html.parser")
    url = urlparse(web_url)
    tag = soup.find_all("a", href = filter(url.netloc))
    link = { kk['href'] for kk in tag}
    if check_link(link) == 1:
        return url._replace(path = link.pop()).geturl()
    else:
        raise Exception(" Using {0}, We find {1} links from {2} \n".format(filter.__name__, len(link), url.geturl()))

def check_link(link):
    if len(link) == 1:
        return 1
    elif len(link) == 0:
        return 0
    else:
        return -1





