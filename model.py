"""Models and database functions for EIS Tracker project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

#sqlalchemy is a python library
#sqlalchemy includes object relational mapping (ORM) and db server

#instantiates object that allows connection to db
db = SQLAlchemy()

#####################################################################
# Model definitions

class EIS_data(db.Model):
    """EIS project displayed on website."""

    __tablename__ = "EIS_data"

    eis_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.String(150), nullable=True)
    title_link = db.Column(db.String(150), nullable =True)
    document = db.Column(db.String(50), nullable=True)
    epa_comment_letter_date = db.Column(db.DateTime, nullable=True)
    federal_register_date = db.Column(db.DateTime, nullable=True)
    agency = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(20), nullable=True)
    download_documents = db.Column(db.String(50), nullable=True)
    download_link = db.Column(db.String(150), nullable=True)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Project title={} state={}>".format(self.title,
                                               self.state)

#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///EIS_data' #location of db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #autosets to True
    db.app = app #instantiates app; connects app to db  
    db.init_app(app) #make active connection

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
