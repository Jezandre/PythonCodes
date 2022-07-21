import requests
from bs4 import BeautifullSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifullSoup()
