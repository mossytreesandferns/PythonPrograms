# Script for getting NASA exoplanet data as a txt file and converting
# it to a csv file

import wget
$ wget "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets" -O "exoplanets.txt"

import csv

with open('Exoplanets.txt', 'r') as txt_file:
    stripped = (line.strip() for line in txt_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Exoplanets.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)

txt_file.close()
csv_file.close()
