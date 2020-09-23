import requests
import time
from bs4 import BeautifulSoup

while True:
    page = 'https://www.repfitness.com/bars-plates/olympic-plates/bumper-plates/rep-black-bumper-plates'
    res = requests.get(page)
    soup = BeautifulSoup(res.content, 'html.parser')
    stock = soup.find_all('p', 'availability out-of-stock')
    print(stock)

    time.sleep(15 * 60)
