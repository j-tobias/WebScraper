from Crawler_Class import Scraper




#if you want to start from a already existing file with urls
#that's also possible and might come in handy when you want to pause the scraping and 
#don't want to start from beginning


#setting up the Scraper
scraper = Scraper('https://www.spiegel.de', 'https://www.spiegel.de')

#Scraper
scraper.scrape()