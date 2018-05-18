import requests
from bs4 import BeautifulSoup
import csv

#open csv from first scrape
csv_data = open('epa_scrape.csv')
reader = csv.reader(csv_data)

#create new file to insert values from second scrape
csv_file = open('second_parse_data.csv', 'write')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['EIS ID', 'Due Date', 'Contact Name', 'Contact Number'])

#iterate over first scrape data and omit first row with title
#identify column with urls and bind to variable
#perform a get request on url and parse next page with project specific info
for i, row in enumerate(reader):
    if i == 0:
        continue    
    url = row[1]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    item = soup.findAll(class_='form-item')

    #capture the EIS id, comment due date, and contact information
    eis_id = item[1].get_text().strip().lstrip('EIS Number')
    comment_due_date = item[4].get_text().strip().lstrip('EIS Comment Due/ Review Period Date').strip().rstrip('00:00:00.0')
    contact_name = item[12].get_text().strip().replace('Contact Name','').lstrip()
    contact_number = item[13].get_text().strip().lstrip('Contact Phone')

    #unpack values into csv into columns
    csv_writer.writerow([eis_id, comment_due_date, contact_name, contact_number])

#close writer by closing file
csv_file.close()
