"""EIS Tracker"""

from jinja2 import StrictUndefined

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, EIS_data

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
    projects_in_ca = EIS_data.query.filter_by(state='CA').all()

    unique_states = EIS_data.query.filter_by(state=state).distinct()

    for state in unique_states:
        state_dict[state] = #query for all projects in this state

    print unique_states
    #query for projects in state
    projects_in_state
    #create diction of unique states
    state_dict = {unique_states: projects_in_state}

    return render_template("homepage.html", projects_in_ca=projects_in_ca)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
