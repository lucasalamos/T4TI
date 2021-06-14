import requests
iso = ['AUS', 'BEL', 'CHL', 'DMA', 'ECU', 'FRA']
with open(i+'.xml', 'w', encoding="utf-8") as f:
        f.write(r.text)