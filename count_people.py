#!/bin/bash/python
###############################################################################
# This code reads in a database of people living between 1900 and 2000 then 
# determines the year with the most living people.
###############################################################################
import numpy as np
import os, sys

# get data filename from user
fname = sys.argv[1]
data = np.genfromtxt(fname,delimiter=',',skip_header=1)

# create dictionary with desired years as keys
def timeframe(start,end):
  years = [x for x in range(start,end+1)]
  init_count = dict()
  for year in years:
    init_count[year] = 0
  return init_count

# create list of years living for each person
# and increment count in timeframe dict
def lifetime(data,count):
  for person in data:
    birth = person[1]
    death = person[2]
    years = [x for x in range(int(birth),int(death)+1)]
    for year in years:
      count[year] += 1
  return count

# count number of people living each year
init_count = timeframe(1900,2000)
living = lifetime(data,init_count)

# determine year with most living
most = [year for year,count in living.iteritems() if count == max(living.values())]

# write year with most living to file
out = open('most_living.txt', 'w')
out.write('The year(s) with the most living people is:\n')
length = 0
for i in most:
  length += 1
  if length == len(most):
    out.write(str(i) + '.')
  else:
    out.write(str(i) + ', ')
out.close()
