from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.ziprecruiter.com/candidate/search?radius=5000&search=entry+level+software+engineer+&location=').text
soup = BeautifulSoup(html_text, 'lxml')
rating = soup.find_all('div')
print(rating)
