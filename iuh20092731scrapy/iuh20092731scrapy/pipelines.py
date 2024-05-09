# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class Iuh20092731ScrapyPipeline:
    def process_item(self, item, spider):
        return item



class CSVDBBooksPipeline:
    def open_spider(self, spider):
        self.file = open('csvdatabooks.csv', 'a', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file, delimiter='$')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow(item.values())
        return item