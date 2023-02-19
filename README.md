# TechReviews-Web-Scraper-bot

Implemented a web crawler using Scrapy library in python to scrape technology reviews and news from https://www.pcmag.com and store it in a csv file.


There are 2 ways you can deploy the crawler:

1)By running the bat file:
Traverse to the directory contains the file ‘spider.bat’ file, using the command “cd ”.
Run the bat file using ‘./spider.bat’ command on the command line.
2)By running the python file:
Navigate to the directory containing the ‘TechReviews.py’file using the command “cd ”.
First step is to move the python file to the ‘spiders’ folder location of the scrapy with all the necessary dependencies of the default scrapy installed.
Run the python file using the following command:
“scrapy crawl pcmag” which will prompt  the crawler to start scraping the data from the webpages.  	

AFter running the scrapy crawler, the resultant scraped data will be collected in the ‘data.csv’ file.
