# Define a function to get the date of an event
def get_event_date(event):
    return event.date


# Define a function to track current users on machines
def current_users(events):
    # Sort events based on date using the previously defined function
    events.sort(key=get_event_date)
    # Initialize an empty dictionary to store machines and their users
    machines = {}
    # Iterate over each event
    for event in events:
        # Check if the machine is not already in the dictionary
        if event.machine not in machines:
            # If not, add the machine to the dictionary and initialize an empty set for users
            machines[event.machine] = set()
        # Check the event type
        if event.type == "login":
            # If it's a login event, add the user to the machine's set of users
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            # If it's a logout event, check if the user is logged in and remove them from the set
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)
    # Return the dictionary containing machines and their current users
    return machines


# Define a function to generate a report of current users on machines
def generate_report(machines):
    # Iterate over each machine and its users in the dictionary
    for machine, users in machines.items():
        # Check if there are any users logged in
        if len(users) > 0:
            # If yes, join the users into a string separated by commas
            user_list = ", ".join(users)
            # Print the machine name and the list of users
            print("{}: {}".format(machine, user_list))


# Define a class to represent events
class Event:
    # Constructor to initialize event attributes
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


# Create a list of events
events = [
    Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
    Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
    Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
    Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
    Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
    Event("2020-01-23 11:24:35", "logout", "mailserver.local", "chris"),
]

# Get current users on machines using the defined function
users = current_users(events)
# Generate and print a report of current users on machines
generate_report(users)
