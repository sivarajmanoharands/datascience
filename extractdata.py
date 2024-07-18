# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:57:20 2023

@author: user
"""


#Prepared by Rick Dobson for MSSQLTips.com
 
#reference libraries
import requests
from bs4 import BeautifulSoup
import os
 
#designate the target page and ready it for processing
#assign a url to myURL
myURL = "https://www.mssqltips.com/sqlserverauthor/57/rick-dobson/"
 
#get url content
r = requests.get(myURL)
 
#parse HTML code
soup = BeautifulSoup(r.content, 'html.parser')
 
#################################################################################
 
#get all the anchor tag elements in the Tips div
#find the div tag with an id attribute of Tips
div_tag = soup.find("div", id="Tips")
 
#find all the anchor tags in the Tips div as a list
Tips_div_anchor_tags = div_tag.find_all("a")
 
#Count all_anchors in the Tips_div_anchor_tags
all_anchor_count = len(Tips_div_anchor_tags)
 
#"""
#optionally display all extracted anchor tags in the IDLE Shell window
print ()
print ('display all Tips_div_anchor_tags')
print ()
 
for anchor_tag in Tips_div_anchor_tags:
    print(anchor_tag["href"])
 
print ()
#"""
 
#################################################################################
 
#select all the category tag elements from Tips_div_anchor_tags
#count and optionally display category_anchors
category_anchors = [Tips_div_anchor_tags[i] for i in range(0, len(Tips_div_anchor_tags),2)]
 
#Count and display category_anchors in the Tips_div_anchor_tags
category_anchor_count = len(category_anchors)
 
print()
print('count of category_anchors', category_anchor_count)
print()
 
#Display all extracted category_anchors with the web site url
for anchor_tag in category_anchors:
    print("https://www.mssqltips.com" + anchor_tag["href"])
 
#################################################################################
 
#select all the tip tag elements from Tips_div_anchor_tags
#count and optionally display category_anchors
tip_anchors = [Tips_div_anchor_tags[i] for i in range(1, len(Tips_div_anchor_tags),2)]
 
#Count and display category_anchors in the Tips_div_anchor_tags
tip_anchor_count = len(tip_anchors)
 
print()
print('count of tip_anchors', tip_anchor_count)
print()
 
#Display all extracted category_anchors
for anchor_tag in tip_anchors:
    print("https://www.mssqltips.com" + anchor_tag["href"])
 
#################################################################################
 
# Get the current working directory
cwd = os.getcwd()
print(cwd)
 
# Change the current working directory
os.chdir("C:/Users/user/project")
 
# Get the new working directory
cwd = os.getcwd()
print(cwd)
 
# opening a file in write mode
f = open("category_anchors.txt", "w")
 
# writing into file
for anchor_tag in category_anchors:
    f.write("https://www.mssqltips.com" + anchor_tag["href"])
    f.write("\n")
 
# closing file
f.close()
 
 
# opening a file in write mode
f = open("tip_anchors.txt", "w")
 
# writing into file
for anchor_tag in tip_anchors:
    f.write("https://www.mssqltips.com" + anchor_tag["href"])
    f.write("\n")
 
# closing file
f.close()