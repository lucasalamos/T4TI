import xml.etree.ElementTree as ET
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe


iso = ['AUS', 'BEL', 'CHL', 'DMA', 'ECU', 'FRA']

country = []
gho = []
sex = []
year = []
ghe = []
age = [] 
display = []
numeric = []
low = []
high = []

for name in iso:
    root = ET.parse(name + '.xml').getroot()
    for i in root.getchildren():
        children = i.getchildren()
        c, ho ,s, y, he, a, d, n, l, h = "", "", "", "", "", "", "", "", "", ""
        for b in children:
            if b.tag == "COUNTRY":
                c = b.text
            elif b.tag == "GHO":
                ho = b.text
            elif b.tag == "SEX":
                s = b.text
            elif b.tag == "YEAR":
                y = b.text
            elif b.tag == "GHECAUSES":
                he = b.text
            elif b.tag == "AGEGROUP":
                a = b.text
            elif b.tag == "Display":
                d = b.text
            elif b.tag == "Numeric":
                n = b.text
            elif b.tag == "Low":
                l = b.text
            elif b.tag == "High":
                h = b.text
            
            
        sex.append(s)
        year.append(y)
        ghe.append(he)
        age.append(a)
        display.append(d)
        numeric.append(n)
        low.append(l)
        high.append(h)
        country.append(c)
        gho.append(ho)
        
        

d = {'country': country, 'gho': gho, 'sex': sex, 'year': year,
    'ghe' : ghe, 
    'age' : age,
    'display' : display,
    'numeric' : numeric,
    'low' : low,
    'high' : high
}


df = pd.DataFrame(data=d)
#print(df)

gc = gspread.service_account(filename='tarea4-316402-ac1ad6c0140b.json')
sh = gc.open_by_key('1sQgtkb3af4Zr9OvUNF-Tj4v-Q2rIF1ZMpkL4cncdRnM')
worksheet = sh.get_worksheet(0)
set_with_dataframe(worksheet, df)
    

   









