import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re


def download(name, link):
    # download file from link, and name it with the name variable
    r = requests.get(link) 
    with open(name,'wb') as f:
        f.write(r.content)

def get_url(soup, filter, web_url):
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

def pdflink_filter(netloc):
    # for different website, we have different filters 
    # These filters are given by regular expression, 
    # the link match these regular expressions is the one we want to get 

    if netloc == 'science.sciencemag.org':
        regex = re.compile("full\.pdf")
    elif netloc == 'www.nature.com':
        regex = re.compile("^/articles/[a-zA-Z0-9]*-[a-zA-Z0-9]*-[a-zA-Z0-9]*-[a-zA-Z0-9]*.pdf")
    else:
        regex = re.compile("\.pdf")

    return regex

def rislink_filter(netloc):
    # for different website, we have different filters 
    # These filters are given by regular expression, 
    # the link match these regular expressions is the one we want to get 
    
    if netloc == 'science.sciencemag.org':
        regex = re.compile("ris$")
    elif netloc == 'www.nature.com':
        regex = re.compile("citation\.ris$")
    else:
        regex = re.compile("ris")
    return regex
    

web_url = "https://www.nature.com/articles/s41586-021-03359-9"

r = requests.get(web_url)
soup = BeautifulSoup(r.content,features="html.parser")

download("temporary.pdf", get_url(soup, pdflink_filter, web_url))
download("temporary.ris", get_url(soup, rislink_filter, web_url))


