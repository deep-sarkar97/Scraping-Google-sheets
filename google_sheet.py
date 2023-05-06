import requests
from bs4 import BeautifulSoup as bs

asin=[]
cntry=[]
url = 'https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM/edit#gid=0'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    for cell in cells[2:3]:
        asin.append(cell.text)
    for cell in cells[3:4]:
        cntry.append(cell.text)


for a,b in zip(asin, cntry):
    print(f"https://www.amazon.{b}/dp/{a}")