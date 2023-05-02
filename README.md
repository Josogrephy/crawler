# crawler
Python crawler to run through URLs to pull certain information

# How to use
1. link.csv in the crawler folder represent the URL to crawl
2. gobispider.py in spiders folder is the spider code
3. cat_list = response.css('p.text-subdued *::text').getall() <-- is the CSS selector. Edit this top pull your require data from the URL
