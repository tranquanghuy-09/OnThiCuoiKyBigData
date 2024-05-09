import scrapy
from iuh20092731scrapy.items import Iuh20092731ScrapyItem

class BooksallproductscrawlerSpider(scrapy.Spider):
    name = "BooksAllProductsCrawler"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com"]

    def start_requests(self):
        yield scrapy.Request(url='https://books.toscrape.com/', callback=self.parse)

    def parse(self, response):
        # allproducts = response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[1]/a/@href').getAll()
        allproducts = response.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li/article/div[1]/a/@href').getall()
        

        for productItem in allproducts:
            item = Iuh20092731ScrapyItem()
            item['productUrl'] = response.urljoin(productItem)
            request = scrapy.Request(url=item['productUrl'], callback=self.parseProductDetailPage)
            request.meta['dataproduct'] = item
            yield request

    def parseProductDetailPage(self, response):
        item = response.meta['dataproduct']
        item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').get()
        item['decriptions'] = response.xpath('//*[@id="content_inner"]/article/p/text()').get()

        # Trích xuất giá từ phần tử <p> có lớp "price_color"
        price_text = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()').get()
        # Loại bỏ ký tự tiền tệ và chuyển đổi giá trị sang dạng số thực
        price = float(price_text.replace('£', '')) if price_text else None
        item['price'] = price

        stock_text = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]').get()
        stock_quantity = int(stock_text.split('(')[1].split()[0]) if stock_text else None
        item['stock'] = stock_quantity
        
        

        # Lấy ra lớp của phần tử <p> chứa rating --  <p class="star-rating Four">
        rating_class = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[3]/@class').get()

        # Hàm chuyển đổi lớp CSS rating thành số tương ứng
        def convert_rating(rating_class):
            if rating_class == 'One':
                return 1
            elif rating_class == 'Two':
                return 2
            elif rating_class == 'Three':
                return 3
            elif rating_class == 'Four':
                return 4
            elif rating_class == 'Five':
                return 5
            else:
                return None
            
        # Tách lớp ra để chỉ lấy được số rating
        rating = rating_class.split(' ')[1] if rating_class else None
        item['rating'] = convert_rating(rating)

        yield item
    
    