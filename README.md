# TechReviews-Web-Scraper-bot

Implemented a web crawler using Scrapy library in python to scrape technology reviews and news from https://www.pcmag.com and store it in a csv file.


There are 2 ways you can deploy the crawler:

1)By running the bat file: <br />
Traverse to the directory contains the file ‘spider.bat’ file, using the command “cd ”.<br />
Run the bat file using ‘./spider.bat’ command on the command line.<br />
2)By running the python file:<br />
Navigate to the directory containing the ‘TechReviews.py’file using the command “cd ”.<br />
First step is to move the python file to the ‘spiders’ folder location of the scrapy with all the necessary dependencies of the default scrapy installed.<br />
Run the python file using the following command:<br />
“scrapy crawl pcmag” which will prompt  the crawler to start scraping the data from the webpages.  	<br />

AFter running the scrapy crawler, the resultant scraped data will be collected in the ‘data.csv’ file.
