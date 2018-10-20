# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class NetshoppingPipeline(object):
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def open_spider(self, spider):
        #可选实现，当spider被开启时，这个方法被调用。
        #输出到tongcheng_pipeline.json文件
        self.file = open('booksearch.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()
        
    def close_spier(selef, spider):
        #可选实现，当spider被关闭时，这个方法被调用
        self.exporter.finish_exporting()
        self.file.close()


