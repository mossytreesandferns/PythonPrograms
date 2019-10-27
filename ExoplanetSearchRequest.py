# Alternative to using WGET

import urllib
import urllib.request
urllib.request.urlretrieve("https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=compositepars", "compositepars.txt")

import csv 
with open('compositepars.txt', 'r') as txt_file:
    stripped = (line.strip() for line in txt_file)
    lines = (line.split(",") for line in stripped if line)
    with open('compositepars.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)

txt_file.close()
csv_file.close()
