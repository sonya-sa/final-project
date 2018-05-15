"""Utility file to seed EIS database from EPA data seed_data/"""

import datetime
from sqlalchemy import func

from model import EIS_data, connect_to_db, db
from server import app

def load_EIS_data(epa_scrape_all_info):
    """Load projects from open_comment.csv into database."""

    print "EIS Data"

    for row in open(epa_scrape_all_info):
        if row[0] == "E":
            continue
        row = row.rstrip()

        print row.split(",")

        #unpack info; row.split(",")
        eis_id, title, title_link, document, comment_letter_date_str, federal_register_date, comment_due_date_str, agency, state, download_documents, download_link, contact_name, contact_phone = row.split(",")

        #ensure strings are stored as datetime objects in database
        if comment_letter_date_str:
            epa_comment_letter_date = datetime.datetime.strptime(comment_letter_date_str, "%m/%d/%y")
        else:
            epa_comment_letter_date = None
        
        if comment_due_date_str:
            comment_due_date = datetime.datetime.strptime(comment_due_date_str, "%m/%d/%y")
        else:
            comment_due_date = None

        #note: this does not include links
        projects = EIS_data(eis_id=eis_id, title=title,
                            document=document, epa_comment_letter_date=epa_comment_letter_date, 
                            federal_register_date=federal_register_date, comment_due_date=comment_due_date, 
                            agency=agency, state=state) 

        #Add to the session to store info
        db.session.add(projects)

    #Once done, commit work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    epa_scrape_all_info = "epa_scrape_all_info.csv"
    load_EIS_data(epa_scrape_all_info)
