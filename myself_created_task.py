from datetime import datetime, timedelta

def calculate_arrive_time():
    start_time = datetime.strptime("07:00", "%H:%M")
    end_time = datetime.strptime("20:00", "%H:%M")
    interval = timedelta(minutes=40)
    specific_time = datetime.strptime(input("Enter the specific time when you going to ride (format is \"HH:MM\"): "), "%H:%M")

    next_available_time = start_time
    while next_available_time <= end_time:
        if specific_time <= next_available_time:
            break
        next_available_time += interval
    next_available_time = next_available_time.strftime("%H:%M")
    next_available_time = 'The closet time when your bus will start its next ride is: ' + str(next_available_time)
    return next_available_time
print(calculate_arrive_time())
