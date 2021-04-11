import requests
from homework1.HtmlPraser import get_url

class web_file:
    def __init__(self, url=None, name="temporary", postfix = None):
        self.url = url
        self.postfix = postfix

    def download(self, link = None , path = None ):
        if not link:
            link = self.url
        if not path:
            path = self.name + self.postfix
        # download file from link, and name it with the name variable
        r = requests.get(link) 
        with open(path ,'wb') as f:
            f.write(r.content)

    def url_get():
        raise Exception("You don't define the url_get()")

class pdf(web_file):
    def __init__(self):
       web_file.__init__(self, postfix = ".pdf")

    def url_get(self,web_url):

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
        
        self.url = get_url(pdflink_filter, web_url)
    


class ris(web_file):
    def __init__(self):
       web_file.__init__(self, postfix = ".ris")
    
    
    def url_get(self,web_url):
        
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

        self.url = get_url(rislink_filter, web_url)

class paper():
    def __init__(self,web_url):
        self.url = web_url
        self.pdf = pdf()
        self.ris = ris()

    def download(self):
        pdf.url_get(web_url)
        pdf.download()

        ris.url_get(web_url)
        ris.download()


        

        




    