import mechanize
from bs4 import BeautifulSoup
import csv
import xml.etree.ElementTree as ET

#comment
# Make the browser object
browser = mechanize.Browser()
browser.set_handle_robots(False)
  
url = 'http://data.parliament.uk/membersdataplatform/services/mnis/members/query/House=Commons%7CIsEligible=true/'

response = browser.open(url)

# Parse the resulting data with Beautiful soup - daft name - great tool

soup = BeautifulSoup(response.read(),'xml')

# response.close()

soupstring = str(soup)#
tree = ET.fromstring(soupstring)

# Pick out one member and get the contents of teh displayas tag
print tree.findall("./Member[0]/DisplayAs")[0].text
# Get all members
memberlist = tree.findall("./Member")

for member in memberlist:
    print member.findall("./DisplayAs")[0].text
    