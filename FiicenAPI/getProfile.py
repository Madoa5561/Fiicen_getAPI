import requests
from bs4 import BeautifulSoup

class Fiicen:

    def __init__(self):
        pass

    def getName(self,id):
        url = "https://fiicen.jp/field/" + id + "/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
            'Content-Type': 'text/html; charset=utf-8'
        }
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")
        displayNameHTML = str(soup.find(class_="display-name"))
        displayName = displayNameHTML.replace('<div class="display-name">','')
        return displayName.replace('</div>','')
        
    def getIcon(self,id):
        url = "https://fiicen.jp/field/" + id + "/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
            'Content-Type': 'text/html; charset=utf-8'
        }
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")
        iconhtml = str(soup.find(class_="account-icon-80"))
        iconhtml = iconhtml.replace("""<img class="account-icon-80" onclick="detailImage('""","")
        iconhtml = iconhtml.replace("""', 'account_icon')" src="/media/account_icon/20177.jpg"/>""","")
        return "https://fiicen.jp" + iconhtml
