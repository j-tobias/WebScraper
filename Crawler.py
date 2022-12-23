import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

class URLScraper:
    def __init__(self, url):
        self.url = url
        self.found_urls = set()
        self.visited_urls = set()
    
    def scrape(self, url = "self.url"):

        if url == "self.url":
            url = self.url

        # Make an HTTP GET request to the website
        response = requests.get(url)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the links in the HTML
        links = soup.find_all('a')

        # Iterate through the links and add them to the visited_urls set
        for link in links:
            link_url = link.get('href')
            if link_url and link_url not in self.visited_urls and link_url not in self.found_urls:
                self.found_urls.add(link_url)

        self.visited_urls.add(url)

    def scrape_recursively(self):

        # Scrape the initial URL
        self.scrape()

        # set Flag
        new_urls_found = True

        # Keep scraping new URLs until no new URLs are found
        while new_urls_found:

            pass





        # code written by ChatGPT
        """
        # Scrape the initial URL
        self.scrape()

        # Keep scraping new URLs until no new URLs are found
        while True:
            new_urls_found = False
            for url in self.visited_urls:
                if url.startswith(self.url):
                    self.url = url
                    self.scrape()
                    new_urls_found = True
                    break

            # Display a progress bar
            pbar = tqdm(total=len(self.visited_urls))
            pbar.update(len(self.results))
            pbar.close()

            #with open("results.csv", mode= "w") as f:
            #    f.writelines(self.visited_urls)

            if not new_urls_found:
                break
        
        """


