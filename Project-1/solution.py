# PROBLEM STATEMENT: Creat a report of the user event in machine. Print those user name list 
# which are login but remove the user name list which are logout.

# First you will create a function for date and denote date as key for events
def get_event_date(event):
    return event.date

# after this you will create a function for user event in machine like if they are logged in there name will
# be added in report but if logged out there name will be removed.
def current_user(events):
    events.sort(key = get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.machine == 'login':
            machines[event.machine].add(event.user)
        elif event.machine == 'logout':
            machines[event.machine].remove(event.user)
            
    return machines

# lastly you will convert it into a report
def generate_report(machines):
    for user, machine in machines.items():
        if len(user) > 0:
            user_list = ', '.join(user)
            print('{}, {}'.format(machine, user_list))