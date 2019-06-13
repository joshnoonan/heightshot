import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def averageL(l):
    return sum(l) / len(l)

with open('1719.csv','r') as f:
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

d['Draymond Green'] += (79,)
d['Kevin Durant'] += (81,)
d['JaVale McGee'] += (84,)
d['Klay Thompson'] += (79,)
d['Quinn Cook'] += (73,)
d['Shaun Livingston'] += (79,)
d['David West'] += (81,)
d['Andre Iguodala'] += (78,)
d['Kevon Looney'] += (81,)
d['Nick Young'] += (79,)
d['Jordan Bell'] += (81,)
d['Damian Jones'] += (84,)
d['Stephen Curry'] += (75,)
d['Zaza Pachulia'] += (83,)
d['Patrick McCaw'] += (79,)
d['DeMarcus Cousins'] += (83,)
d['Alfonzo McKinnie'] += (80,)
d['Andrew Bogut'] += (84,)
d['Jonas Jerebko'] += (82,)
d['Jacob Evans'] += (78,)




x = [d[key][1] for key in d.keys()] #x-var = height
y = [d[key][0] for key in d.keys()] #y-var = avg shot dist
keys = [key for key in d.keys()]

plt.scatter(x, y, zorder = 10)
plt.xlabel('Height (in inches)')
plt.xlim(left = 72, right = 88)
plt.ylim(bottom = 0, top = 25)
plt.ylabel('Average shot distance (in feet)')
plt.title('Height vs Avg. Shot Distance for Warriors players (2017-2019)')

i = 0
for x,y in zip(x,y): #annotate each point with respective player
    plt.text(x * (1 + 0.003), y * (1 + 0.004) , keys[i], fontsize=5.2)
    i += 1
plt.text(70,-2.3,'Data Source: stats.nba.com', fontsize=7)
plt.axhspan(15,25, .38,1,  facecolor='lightgrey')
plt.savefig('GSscatter.pdf')
plt.show()
