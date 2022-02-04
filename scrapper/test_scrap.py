from bs4 import BeautifulSoup
import requests

url = 'https://www.climatempo.com.br/'
req = requests.get(url).content

soup = BeautifulSoup(req, 'html.parser')
# print(soup.prettify())

temp = soup.find_all('p', class_="-gray _flex _align-center")
for t in temp:
    minima, maxima = t.text.split()
    print(f'\nMinima: {minima} Máxima: {maxima}\n')
    break

