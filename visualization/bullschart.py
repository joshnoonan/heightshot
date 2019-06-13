import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def averageL(l):
    return sum(l) / len(l)

with open('9698.csv','r') as f:
        csvf = csv.reader(f)
        result = []
        for row in csvf:
            if row[1].isdigit(): result.append(row) 

d ={}

    
for row in result: #map player names to all shot distances
    if row[4] not in d.keys():
        d[row[4]] = (float(row[16]),) 
    else:
        d[row[4]] += (float(row[16]),)

for key in d.keys():
    d[key] = (averageL(d[key]),) #compute average shot distance

# add heights

d['Luc Longley'] += (86,)
d['Jason Caffey'] += (80,)
d['Ron Harper'] += (78,)
d['Michael Jordan'] += (78,)
d['Dennis Rodman'] += (79,)
d['Scottie Pippen'] += (80,)
d['Toni Kukoc'] += (83,)
d['Bison Dele'] += (83,)
d['Jud Buechler'] += (78,)
d['Randy Brown'] += (75,)
d['Steve Kerr'] += (75,)
d['Robert Parish'] += (84,)



x = [d[key][1] for key in d.keys()] #x-var = height
y = [d[key][0] for key in d.keys()] #y-var = avg shot dist
keys = [key for key in d.keys()]

plt.scatter(x, y, c= 'r', zorder = 10)
plt.xlabel('Height (in inches)')
plt.xlim(left = 72, right = 88)
plt.ylim(bottom = 0, top = 25)
plt.ylabel('Average shot distance (in feet)')
plt.title('Height vs Avg. Shot Distance for Chicago Bulls players (1996-1998)')

i = 0
for x,y in zip(x,y): #annotate each point with respective player
   plt.text(x * (1 + 0.005), y * (1 + 0.005) , keys[i], fontsize=6.9)
   i += 1
plt.text(70,-2.3,'Data Source: stats.nba.com', fontsize=7)
plt.axhspan(15,25, .38,1,  facecolor='lightgrey')
plt.savefig('CHIscatter.pdf')
plt.show()
