#Importing Libraries
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import FormRequest

class TechReview(scrapy.Spider):
    name = "pcmag"  #name of the crawler
    start_urls = [
        'https://www.pcmag.com/reviews/',
        'https://www.pcmag.com/news'
    ]
    allowed_domains=['pcmag.com']
    def parse(self, response): 
        
        #Obtaining links
        links = response.css("div.w-full.py-4.border-b.border-gray-lighter a::attr(href)").extract()
        
        #For each link, we scrape the article inside
        for link in links:
            yield response.follow(link, self.parse_next_page)                                                                                                                                   
        
        next_page = response.css("a[rel='next']::attr(href)").extract_first()
        yield response.follow(next_page, callback=self.parse)

    def parse_next_page(self, response):
        # Extract the paragraphs from the next page
        # Yield the extracted data as an item
        yield {
             'title': response.css("h1::text").get(),
             'review': response.css("p::text").getall(),
             'link': response.url
        }

# Creating Process

#Settings Configuration      
process = CrawlerProcess(settings= {
    'FEED_URI': 'data.csv',
    'FEED_FORMAT': 'csv',
    'FEED_STORAGE_APPEND': True
})


#Starting the crawler and creating a csv file to store the data. 
process.crawl(TechReview)
process.start()







