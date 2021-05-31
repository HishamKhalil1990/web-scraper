import re
import requests
from bs4 import BeautifulSoup
URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(URL,word):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser") 
    searched_word = word
    results = soup.find_all(text = searched_word)
    return len(results)

def get_citations_needed_report(URL,word):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser") 
    searched_word = word
    results = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    res_list = []
    for res in results:
        if not res_list or res.parent.text not in res_list:
            res_list.append(res.parent.text)  
    string = """"""
    string = '\n'.join(res_list).strip() 
    return string

if __name__ == "__main__":
    print(get_citations_needed_count(URL,'citation needed'))
    print(get_citations_needed_report(URL,'citation needed'))