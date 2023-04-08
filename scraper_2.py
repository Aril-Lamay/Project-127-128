from bs4 import BeautifulSoup
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(START_URL)
print(page)

stars_data = []

soup = BeautifulSoup(page.text,"html.parser")

star_table = soup.find_all("table")

table_rows = star_table[7].find_all("tr")

temp_list = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Mass = []
Distance = []
Radius = []
#data = pd.DataFrame(temp_list)
#print(data)
for i in range(1, len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
df2.to_csv("Dwarf_stars.csv")
print(df2)