import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox(executable_path='G:\exam\webdriver\geckodriver.exe')
driver.get('xxx')

point1 = []
point2 = []

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs={'class': 'class'}):
    name = a.find('a')
    if name not in point1:
        point1.append(name.text)

for b in soup.findAll(attrs={'class': 'otherclass'}):
    name2 = b.find('span')
    point2.append(name.text)

res1 = pd.Series(point1, name = 'First')
res2 = pd.Series(point2, name = 'Second')
df = pd.DataFrame({'First': res1, 'Second': res2})
df.to_csv('result.csv', index=False, encoding='utf-8')

