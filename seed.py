"""Utility file to seed EIS database from EPA data seed_data/"""

from sqlalchemy import func
from server import app

def load_open_comment(open_comment_file):
    """Load projects from open_comment.csv into database."""

    #strip file
    for i, row in open(open_comment_file):
        row = row.rstrip()
        #unpack info; row.split("")

    data = 

    #Add to the session to store info
        db.session.add(data)

    #Once done, commit work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

open_comment_file = "seed_data/open_comment.csv"
load_open_comment(open_comment_file)
