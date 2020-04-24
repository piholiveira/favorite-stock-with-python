import requests
from bs4 import BeautifulSoup
import re

acoes = ['ITSA4.SA', 'FLRY3.SA', 'TOTS3.SA', 'B3SA3.SA', 'ENBR3.SA', 'HGLG11.SA', 'KNRI11.SA']

url = 'https://br.financas.yahoo.com/quote/'

for i in acoes:
    requisicao = requests.get(url + str(i) + '/') #get url with stock
    soup = BeautifulSoup(requisicao.content, 'html.parser') #get all html page
    html_filter = soup.find_all('span') #filter by span tag
    regex_filter = re.findall(r'.[0-9],[0-9]{1,}%', str(html_filter)) #filter with regex
    print('Ativo ' +  str(i) + ' ' + str(regex_filter))