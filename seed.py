"""Utility file to seed EIS database from EPA data seed_data/"""

import datetime
from sqlalchemy import func

from model import EIS_data, connect_to_db, db
from server import app

def load_EIS_data(epa_scrap_all_info):
    """Load projects from open_comment.csv into database."""

    print "EIS Data"

    for i, row in open(epa_scrap_all_info):
        row = row.rstrip()
        eis_id, title, title_link, document, epa_comment_letter_date, 
        federal_register_date, comment_due_date, agency, state, download_documents, download_link, contact_name, contact_phone = row.split(",")

        projects = EIS_data(eis_id=eis_id, title=title, title_link=title_link
                            document=document, epa_comment_letter_date=epa_comment_letter_date, 
                            federal_register_date=federal_register_date, comment_due_date=comment_due_date, 
                            agency=agency, state=state, download_documents=download_documents, download_link=download_link) 
        #unpack info; row.split("")


        #Add to the session to store info
        db.session.add(projects)

    #Once done, commit work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

open_comment_file = "seed_data/open_comment.csv"
load_open_comment(open_comment_file)
