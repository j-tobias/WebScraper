#Imports
import urllib3
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import json
import codecs
import requests



class Scraper:

    def __init__ (self, url:str, base:str, starting_urllist:list =None):
        """
        url = starting url of the website https://www.spiegel.de !!!! ALWAYS in the format
        
        """ 
        #"ISO 8859-15" also a common encoding   
        self.current_html = None
        self.urllist = starting_urllist or [url]
        self.url = url
        self.base = base

        #loading of CONFIG file values
        with open('CONFIG.json', mode='r') as conf:
            config_dict = json.load(conf)

        self.encoding = config_dict['encoding']
        self.iterations = config_dict['iterations']
        self.html_filename = config_dict['urls_file']

    def get_urls_from_url (self, url:str) -> list:
        """
        returns a list of all urls from the url

        url: 'https://www.spiegel.de'
        """        
    
        try:
            html_ = requests.get(url)
            html = html_.content
            html_.close()

            soup = bs(html, 'html.parser')
            urls = []
            for link in soup.find_all('a'):
                if self.base in str(link.get('href')):
                    urls.append(link.get('href'))
        except Exception as e:
            urls = []


        return urls

    def savetofile (self, urllist: list):
        """
        saves a urllist to a file
        """
        with open(self.html_filename, mode='w') as file:
            #i know there is the option with file.writelines but it happens that
            #a url can be written to the file because of an encoding error and therefore the
            #process then wouldn't stop
            for url in urllist:
                try:
                    file.write(f'{url}\n')
                except:
                    pass

    def scrape (self)-> list:
        """
        This method scrapes a starting url for defined iterations

        url: 'https://www.spiegel.de'
        """

        for i in tqdm(range(self.iterations)):

            new_urls_from_iteration = []
            for url in tqdm(self.urllist):
                new_urls = self.get_urls_from_url(url)
                new_urls_from_iteration = [*new_urls,*new_urls_from_iteration]
            
            self.urllist = [*new_urls_from_iteration,*self.urllist]
            self.urllist = list(dict.fromkeys(self.urllist))

            self.savetofile(self.urllist)


