import requests
from bs4 import BeautifulSoup
import csv
#from model import EIS_data

#create csv file to save data
#pass in csv to writer method
#create column names in csv
csv_file = open('epa_scrape.csv', 'write')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Title Link', 'Document', 'EPA Comment Letter Date', 'Federal Register Date', 'Agency', 'State', 'Download Documents', 'Document Link'])

#get request EIS data from EPA and bind to page variable
page = requests.get("https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=44C7A9270B513A7577A50349737B3D3A?d-446779-p=1&d-446779-o=2&search=&d-446779-s=1&commonSearch=openComment#results")

#creates an instance of the BeautifulSoup class to parse
soup = BeautifulSoup(page.content, 'html.parser')

#list comprehension used to parse multiple pages
#pg1, pg2, pg3 = (BeautifulSoup(requests.get(page).content, "html.parser"), for page in ["https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=429DC8B149384A480DA14E00931C70D9?search=&commonSearch=openComment#results", "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=429DC8B149384A480DA14E00931C70D9?d-446779-p=2&search=&commonSearch=openComment#results", "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=429DC8B149384A480DA14E00931C70D9?d-446779-p=3&search=&commonSearch=openComment#results"])
#urls = ["https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=429DC8B149384A480DA14E00931C70D9?search=&commonSearch=openComment#results", "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=429DC8B149384A480DA14E00931C70D9?d-446779-p=2&search=&commonSearch=openComment#results", "https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/search;jsessionid=429DC8B149384A480DA14E00931C70D9?d-446779-p=3&search=&commonSearch=openComment#results"]
#soup = (BeautifulSoup(requests.get(page).content, "html.parser") for page in urls)

#find all information for table
table = soup.find('table', class_='responsive-table')

rows = table.find('tbody').findAll('tr')

#prints EIS database table, including href
#print table.prettify()
#print table.get_text()

#add values to csv file by unpacking values into columns; nest in for loop
for row in rows:
    columns = row.findAll('td')

    title = columns[0].get_text().strip()
    title_link = columns[0].find('a').get('href')
    document = columns[1].get_text().strip()
    epa_comment_date = columns[2].get_text().strip()
    fed_reg_date = columns[3].get_text().strip()
    agency = columns[4].get_text().strip()
    state = columns[5].get_text().strip()
    download_docs = columns[6].get_text().strip()
    download_docs_link = columns[6].find('a').get('href')

    #writes column values to csv
    csv_writer.writerow([title, 'https://cdxnodengn.epa.gov' + title_link, document, epa_comment_date, fed_reg_date, agency, state, download_docs, 'https://cdxnodengn.epa.gov' + download_docs_link])

#closes cvs; done writing values
csv_file.close()