import requests
from bs4 import BeautifulSoup
import csv

#create csv file to save data
#pass in csv to writer method
#create column names in csv
# csv_file = open('epa_scrape.csv', 'write')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['title','link','federal register date', 'agency', 'state', 'download docs'])

#get request EIS data from EPA and bind to page variable
page = requests.get("https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=44C7A9270B513A7577A50349737B3D3A?d-446779-p=1&d-446779-o=2&search=&d-446779-s=1&commonSearch=openComment#results")

#creates an instance of the BeautifulSoup class to parse
soup = BeautifulSoup(page.content, 'html.parser')

#find all information for table
table = soup.find('table', class_='responsive-table')

# #save data by column; nest in for loop
#     title =
#     link =
#     fed_reg_date =
#     agency =
#     state = 
#     downloads = 


#     #add values to csv file by unpacking values into columns; nest in for loop
#     csv_writer.writerow([title, link, fed_reg_date, agency, state, downloads])

# csv_file.close()

#prints EIS database table, including href
print table.prettify()
#print table.get_text()
#for i in table.descendants:
    #print i

#for i in table.children:
    #print i
#for link in table.find_all('a'):
    #print link.get('href')






