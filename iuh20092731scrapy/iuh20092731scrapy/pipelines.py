# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

import json

import pymongo
import os
from dotenv import load_dotenv
from scrapy.exceptions import DropItem


# Load environment variables from .env file
load_dotenv()

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
    
class JsonDBBooksPipeline:
    def process_item(self, item, spider):
        self.file = open('jsondatabooks.json','a',encoding='utf-8')
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        self.file.close()
        return item
    
class MongoDBUnitopPipeline:
    def __init__(self):
        print('os.environ.get(\'MONGO_URI\')', os.environ.get('MONGO_URI'))
        self.client = pymongo.MongoClient(os.environ.get('MONGO_URI'))
        self.db = self.client[os.environ.get('MONGO_DB')]
    
    def process_item(self, item, spider):
        collection =self.db[os.environ.get('MONGO_COLLECTION')]
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")