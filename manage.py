from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml' )
    name_html_tags = soup.find_all('td')
    for name in name_html_tags:
        print(name.text)