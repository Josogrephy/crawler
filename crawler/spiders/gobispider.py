import scrapy

class gobiSpider(scrapy.Spider):
    name = "gobiSpider"
    def start_requests(self):
        # Use CSV import to import the list of URL
        with open('links.csv', 'r') as fil:
            urls = fil.read().split('\n')
        # Spider to crawl through each URL in the CSV
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        # crawl and parse
        #save it into a CSV
    def parse(self, response):
        # Find CSS selector
        cat_list = response.css('p.text-subdued *::text').getall()[0:5]
        # Crawl URL
        cat_url = response.url
        cat_str = ''.join(cat_list)
        # build url, pulled data
        cat_str =  cat_url+ "," + cat_str + "\n"
        f = open("catlist.csv", "a")
        f.write(cat_str)
        f.close()