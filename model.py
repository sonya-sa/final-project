"""Models and database functions for EIS Tracker project."""

from flask_sqlalchemy import SQLAlchemy
# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()

#####################################################################
# Model definitions

class EIS_data(db.Model):

    __tablename__ = "EIS_data"

    title = db.Column(db.String(64), nullable=True)
    document = db.Column(db.String(64), nullable=True)
    epaCommentLetterDate = db.Column(db.String(64), nullable=True)
    federalRegisterDate = db.Column(db.String(64), nullable=True)
    agency = db.Column(db.String(64), nullable=True)
    state = db.Column(db.String(64), nullable=True)
    downloadDocuments = db.Column(db.String(64), nullable=True)

#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
