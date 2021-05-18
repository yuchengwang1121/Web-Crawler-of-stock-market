from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests

class Stock(ABC):# 股票抽象類別

    def __init__(self, number):
        self.number = number

    @abstractmethod
    def scrape(self):
        pass

class TWSE(Stock):

    def scrape(self):
        response = requests.get(
            "https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html"
        )

        soup = BeautifulSoup(response.content, "html.parser")

        cards = soup.find_all(
            'div', {'class': 'dataTables_wrapper no-footer'}, limit=15)
 
        content = ""
        for card in cards:
 
            title = card.find(  # name
                "td", {"class": "dt-head-center dt-body-left"}).getText()
 
            value = card.find(  # dollars
                "div", {"class": "dt-head-center dt-body-right"}).getText()
 
 
            #將取得的name、value連結一起，並且指派給content變數
            content += f"{title} \n{value}元 \n\n"
 
        return content
