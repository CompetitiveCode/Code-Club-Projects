#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = 'Favourite Pets'
piechart.add('Dog', 6)
piechart.add('Cat', 4)
piechart.add('Hamster', 3)
piechart.add('Fish', 2)
piechart.add('Snake', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = 'Favourite Sports'
barchart.add('Cricket', 6)
barchart.add('Football', 4)
barchart.add('Marathon', 3)
barchart.add('Basketball', 2)
barchart.add('Baseball', 1)
barchart.render()

piechart1 = pygal.Pie()
piechart1.title = 'Favourite Series'
barchart1 = pygal.Bar()
barchart1.title = 'Favourite Series'
file = open('series.txt','r')
for line in file.read().splitlines():
    if line:
        label,value=line.split('-')
        piechart1.add(label, int(value))
        barchart1.add(label, int(value))
file.close()
piechart1.render()
barchart1.render()