import requests
from homework1.HtmlPraser import get_url
import shutil
from homework1.RisOperation import generate_name_from_ris
import os 

class web_file:
    def __init__(self, url=None, name="temporary", postfix = None, directory = None):
        self.url = url
        self.postfix = postfix
        if not directory:
            self.directory = directory
        else:
            self.directory = os.getcwd()


    def download(self, link = None , path = None ):
        if not link:
            link = self.url
        if not path:
            path = self.path()
        # download file from link, and name it with the name variable
        r = requests.get(link) 
        with open(path ,'wb') as f:
            f.write(r.content)

    def url_get(self):
        raise Exception("You don't define the url_get()")

    def rename(self, newname):
        oldpath = self.path()
        self.name = newname
        newpath = self.path()
        shutil.move(oldpath, newpath)

    def path(self):
        if not self.directory :
            path = self.directory + self.name + self.postfix
        else:
            path = self.name + self.postfix
        return path

        
class pdf(web_file):
    def __init__(self, directory = None):
       web_file.__init__(self, postfix = ".pdf", directory= directory)

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
    def __init__(self, directory = None):
       web_file.__init__(self, postfix = ".ris", directory= directory)
    
    
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
    def __init__(self, web_url, pdf_directory = None, ris_directory = None):
        self.url = web_url
        self.pdf_dir = pdf_directory
        self.ris_dir = ris_directory
        self.pdf = pdf(directory= self.pdf_dir)
        self.ris = ris(directory= self.ris_dir)

    def download(self):
        self.pdf.url_get(web_url)
        self.pdf.download()

        self.ris.url_get(web_url)
        self.ris.download()

        # generate name from .ris file and rename both pdf and ris files
        name = generate_name_from_ris(ris.path())
        self.pdf.rename(name)
        self.ris.rename(name)
        



        

        




    