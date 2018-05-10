import requests
from bs4 import BeautifulSoup
import csv
#from model import EIS_data

#create csv file to save data
#pass in csv to writer method
#create column names in csv
csv_file = open('epa_scrape.csv', 'write')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Document', 'EPA Comment Letter Date', 'Federal Register Date', 'Agency', 'State', 'Download Documents'])

#get request EIS data from EPA and bind to page variable
page = requests.get("https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=44C7A9270B513A7577A50349737B3D3A?d-446779-p=1&d-446779-o=2&search=&d-446779-s=1&commonSearch=openComment#results")

#creates an instance of the BeautifulSoup class to parse
soup = BeautifulSoup(page.content, 'html.parser')

#find all information for table
table = soup.find('table', class_='responsive-table')

rows = table.find('tbody').findAll('tr')

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
#print table.prettify()
#print table.get_text()
#for i in table.descendants:
    #print i

#for i in table.children:
    #print i
# all_links = []

for row in rows:
    columns = row.findAll('td')

    title = columns[0].get_text().strip()
    title_link = columns[0].find('href')
    document = columns[1].get_text().strip()
    epa_comment_date = columns[2].get_text().strip()
    fed_reg_date = columns[3].get_text().strip()
    agency = columns[4].get_text().strip()
    state = columns[5].get_text().strip()
    download_docs = columns[6].get_text().strip()
    download_docs_link = columns[6].find('href')

    csv_writer.writerow([title, title_link, document, epa_comment_date, fed_reg_date, agency, state, download_docs, download_docs_link])

csv_file.close()