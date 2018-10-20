from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from scrapy.http import HtmlResponse

class Driver():

    
    BUSY=0
    IDEL=1
    
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.status=self.IDEL
    
    def get(self,url):
        if self.status:
            self.status=self.BUSY            
            self.driver.implicitly_wait(10)
            self.driver.get(url)
            content = self.driver.page_source
            self.status=self.IDEL
            return content
    def status(self):
        return self.status
    
    def close(self):
        self.driver.close()
         
    
    
class WebDriver():
    
    
    driver=[]
    url_queue=[]
    number=3

    def __init__(self,number=3):
        
        for x in range(number):
            dr=Driver()
            dr.get('https://www.taobao.com')
            self.driver.append(dr)
            
        self.number=number
        
        
    def __run__(self):
        
        while(True):
            if len(url_queue)!=0:
                for x in range(number):
                    if self.driver[x].status:
                        self.driver[x].get(url_queue.pop())
                        break
            time.sleep(5)
            
    def close(self):
        for x in range(self.number):
            self.driver[x].close()
        
    
    def get(self,url):
        
        while(True):
            for x in range(self.number):
                if self.driver[x].status:
                    return self.driver[x].get(url)
        
        
    
    def __push(self,url):
        self.url_queue.append(url)
        
    
    def __pop(self):
        if len(self.url_queue)!=0:
            return self.url_queue.pop(0)
    
