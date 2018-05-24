"""EIS Tracker"""

import datetime

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, EIS_data, State, Project_State

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# If you use an undefined variable in Jinja2, it fails silently.
# Now, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage."""

    # Grab data from the database
    # Format data if necessary to make it easy to render
    # Pass data to jinja template
    # projects_in_ca = EIS_data.query.filter_by(state='CA').all()
    # print projects_in_ca

    # unique_states = EIS_data.query.filter_by(state=state).distinct()

    # #create diction of unique states
    # state_dict = {}

    # #query for projects in state
    # for state in unique_states:
    #     #query for all projects in this state
    #     state_dict[state] = EIS_data.query.filter_by(state=state).all()

    #print state_dict

    #get all projects and their info
    # all_projects = Project_State.query.filter_by(State.state_id).all()

    # project_in_state = EIS_data.query.group_by(EIS_data.project_state).all()

    states = State.query.all()

    states_with_projects = []

    for state in states[1:]:
        # query for all projects in this state and put them into a dictionary.
        state_project_relationships = Project_State.query.filter_by(state_id=state.state_id).all()
        if len(state_project_relationships) > 0:
            projects_in_state = []
            for relationship in state_project_relationships:
                projects_in_state += EIS_data.query.filter_by(eis_id=relationship.eis_id).all()

            for project in projects_in_state:
                #project.comment_due_date = project.comment_due_date.strftime('%m/%d/%y')
                print project
                print type(project.comment_due_date)
            states_with_projects.append([state, projects_in_state])

                # print type(project.comment_due_date)
                # if type(project.comment_due_date) == 'datetime.datetime':
                #     project.comment_due_date =  project.comment_due_date.strftime('%m/%d/%y')
                #     print type(project.comment_due_date)
                #     print project.comment_due_date 
    #         states_with_projects.append([state, projects_in_state])
    # for state, projects in states_with_projects:
    #     print state
    #     for project in projects:
    #         project.comment_due_date =  project.comment_due_date.strftime('%m/%d/%y') 
    #         print project.comment_due_date
    #for loop over each object within list of objects
    #create dict = name as they appear on table, projects info 
    return render_template("homepage.html", states_with_projects=states_with_projects)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")