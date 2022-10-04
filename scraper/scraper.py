import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

service = Service(executable_path="G:\exam\webdriver\geckodriver.exe")
driver = webdriver.Firefox(service=service)
url = "https://www.gundammad.co.uk/home.php"
driver.get(url)### test website / alternative https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/

point1 = []
point2 = []

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs={'class': 'new-prod-link'}):
    name = a.find('a')
    if name not in point1:
        point1.append(name.text)

for b in soup.findAll(attrs={'class': 'currency'}):
    name2 = b.find('span')
    point2.append(name.text)

res1 = pd.Series(point1, name = 'First')
res2 = pd.Series(point2, name = 'Second')
df = pd.DataFrame({'First': res1, 'Second': res2})
df.to_csv('result.csv', index=False, encoding='utf-8')

exit()

### gives acceptable results from simple websites, anything more modern requires taking the page apart more

"""
#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="db_user",
    password="db_user_passwd",
    host="localhost",
    database="employees")
cur = conn.cursor() 

#retrieving information 
some_name = "Georgi" 
cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,)) 

for first_name, last_name in cur: 
    print(f"First name: {first_name}, Last name: {last_name}")
    
#insert information 
try: 
    cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()
"""