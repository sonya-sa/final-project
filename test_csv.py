def load_States(states_coordinates):
    """Load states from state_coordinates.csv into database."""

    print "State Coordinates"

    #parsing csv:
    for row in open(states_coordinates):
        row = row.rstrip()

        #unpack info; row.split(",")
        state_id, geo_lat, geo_long = row.split(",")
        print geo_lat
        print geo_long
        print state_id

        geo_lat = float(geo_lat)
        geo_long = float(geo_long)


        #states = State(state_id=state_id, geo_lat=geo_lat, geo_long=geo_long)

if __name__ == "__main__":

    states_coordinates = "state_coordinates_example.csv"
    load_States(states_coordinates)