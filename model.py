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

    __tablename__ = "eis_data"

    eis_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150), nullable=True)
    title_link = db.Column(db.String(1000), nullable =True)
    document = db.Column(db.String(50), nullable=True)
    epa_comment_letter_date = db.Column(db.DateTime, nullable=True)
    federal_register_date = db.Column(db.DateTime, nullable=True)
    comment_due_date = db.Column(db.DateTime, nullable=True)
    agency = db.Column(db.String(50), nullable=True)
    #state = db.Column(db.String(50), nullable=True)
    download_documents = db.Column(db.String(50), nullable=True)
    download_link = db.Column(db.String(1000), nullable=True)
    
    #this is useful for debugging; instead of the object location in memory, we get the following info
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Project title={} state={}>".format(self.title,
                                               self.state)

class State(db.Model):
    """All states"""

    __tablename__ = "states"

    state_id = db.Column(db.String(3), primary_key= True)
    geo_lat = db.Column(db.Float(15), nullable=False)
    geo_long = db.Column(db.Float(15), nullable=False)

    #this is useful for debugging; instead of the object location in memory, we get the following info
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<State state_id={}>".format(self.state_id)

class Project_State(db.Model):

    __tablename__ = "project_state"

    project_state_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_id = db.Column(db.String, db.ForeignKey('states.state_id'), nullable=False)
    eis_id = db.Column(db.Integer, db.ForeignKey('eis_data.eis_id'), nullable=False)

    # Defines relationship to eis_data
    eis_info = db.relationship("EIS_data",
                           backref=db.backref("project_state",
                                              order_by=project_state_id))


    # Defines relationship to 
    state = db.relationship("State",
                            backref=db.backref("project_state",
                                               order_by=project_state_id))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Project States project_state_id= {} state_id={}>".format(self.project_state_id, self.state_id)

#add relationship and back ref

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
