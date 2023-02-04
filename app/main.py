from bs4 import BeautifulSoup
import requests

URL = "https://maasaablog.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html')

tag = soup.select(selector=".logo > a > span")[0]
print(tag.text)
