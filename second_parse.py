import requests
from bs4 import BeautifulSoup
import csv

#urls = [ 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=249649', 'https://cdxnodengn.epa.gov/cdx-enepa-II/public/action/eis/details?eisId=249641']

csv_data = open('epa_scrape.csv')
reader = csv.reader(csv_data)
for i, row in enumerate(reader):
    if i == 0:
        continue
    url = row[1]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    item = soup.findAll(class_='form-item')
    #rows = item.find('tbody').findAll('tr')
    
    print item[1].get_text().strip().lstrip('EIS Number')
    print item[4].get_text().strip().lstrip('EIS Comment Due/ Review Period Date').strip().rstrip('00:00:00.0')

csv_file = open('second_parse_data', 'write')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['EIS ID', 'Due Date'])


    
    # for row in rows:
    #     columns = row.findAll('td')
    #     EIS_number = columns[1].get_text().strip()