# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from NetShopping.items import NetshoppingItem

import pandas as pd
import requests
import re
from urllib.parse import unquote
from NetShopping.server import WebDriver
from scrapy.http import Response

class NetshoppingSpider(scrapy.Spider):
    name = 'NetShopping'
    allowed_domains = ['taobao.com']
    start_urls = []
    category = 'taobao'
    

    
    def __init__(self, category=None, *args, **kwargs):
        super(NetshoppingSpider, self).__init__(*args, **kwargs)  
        self.category= category

        self.keys=self.loadkeys('booklist.csv')
        self.driver=WebDriver()

        for key in self.keys:
            self.start_urls.append(self.searchurl(key))
        
        '''
        self.cookie=loadcookie('cookie.txt')
        
        self.driver = webdriver.Chrome()
        self.driver.get('https://taobao.com/')
        
        for name,val in self.cookie.items():
            self.driver.add_cookie({'name':name,'value':val})
        '''
                 
    def parse(self, response):
        total=36
        pre_box = '//div[starts-with(@class,"item J_MouserOnverReq") and @data-index="'#index from 0
        after_box = '"]'
        
        key=re.search('q=.*?&',response.url).group()
        
        if type(key) is str:
            key=key[2:-1]
            
        content=self.driver.get(response.url)
        
        new_resp=Response(response.url,body=content)
        
        for i in range(total):
            item = ItemLoader(NetshoppingItem(), response=new_resp)
            item.add_xpath('name',pre_box + str(i) +after_box+'//img/@alt')
            item.add_value('keyword',unquote(key))
            item.add_xpath('price',pre_box + str(i) +after_box+'//div[@class="row row-2 title"]/a/@trace-price')
            item.add_xpath('shop_name',pre_box + str(i) +after_box+'//div[@class="shop"]//span/text()')
            item.add_xpath('shop_url',pre_box + str(i) +after_box+'//div[@class="shop"]/a/@href')
            item.add_xpath('item_url',pre_box + str(i) +after_box+'//div[@class="row row-2 title"]/a/@href')
            yield item.load_item()


       
    def getResponse(self,url):
        return self.drvier.get(url)

        

    def loadkeys(self,path):
        data=pd.read_csv(path,header=None)
        return data.iloc[:,0].values
    
    def loadcookie(self,path):
        with open(path,'r') as f:
            text=f.read()
        
        items=text.split(';')
        ret={}
        for item in items:
            vals=item.split('=',maxsplit=1)
            ret[vals[0]]=vals[1]
            
        return ret
        

    def searchurl(self,key):
        return 'https://s.taobao.com/search?'+\
        'q='+key+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20181002&ie=utf8'
        
     

    

        
    
    
    
    
    
    
