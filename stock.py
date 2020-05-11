import requests
from bs4 import BeautifulSoup
import re

acoes = ['ITSA4.SA', 'FLRY3.SA', 'TOTS3.SA', 'B3SA3.SA', 'ENBR3.SA', 'HGLG11.SA', 'BMLC11B.SA']

url = 'https://br.financas.yahoo.com/quote/'

#dict contendo todas as empresas e ações
companies = {}

for i in acoes:
    requisicao = requests.get(url + str(i) + '/') #get url with stock
    soup = BeautifulSoup(requisicao.content, 'html.parser') #get all html page
    value = soup.find_all('span')
    regex_filter = re.findall(r'.[0-9]{1,2},[0-9]{1,}%', str(value)) #filter with regex
       
    business_tag = soup.find_all('h1') #filter by h1 tag
    companies[i] = {'name': business_tag[0].decode_contents(), 'value': regex_filter}

for i in companies.keys():
  find_low = bool(re.findall(r'value(.*\-[0-9].*)', str(companies[i])))
  if find_low == True:
    print(f"{companies[i]['name']} - {companies[i]['value']}")  