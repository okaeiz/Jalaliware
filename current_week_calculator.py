import datetime

def current_week_calculator():
    current_time = datetime.datetime.now()
    day_of_week = current_time.weekday()
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    day_of_week_string = days[day_of_week]
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    match day_of_week_string:
        case "Monday":
            current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            days_to_subtract = 2
            new_time = (current_time - datetime.timedelta(days=days_to_subtract))
            current_week_start = new_time.strftime('%Y-%m-%d 00:00:00')                 
        case "Tuesday":
            current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            days_to_subtract = 3
            new_time = (current_time - datetime.timedelta(days=days_to_subtract))
            current_week_start = new_time.strftime('%Y-%m-%d 00:00:00')                 
        case "Wednesday":
            current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            days_to_subtract = 4
            new_time = (current_time - datetime.timedelta(days=days_to_subtract))
            current_week_start = new_time.strftime('%Y-%m-%d 00:00:00')                 
        case "Thursday":
            current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            days_to_subtract = 5
            new_time = (current_time - datetime.timedelta(days=days_to_subtract))
            current_week_start = new_time.strftime('%Y-%m-%d 00:00:00')                 
        case "Friday":
            current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            days_to_subtract = 6
            new_time = (current_time - datetime.timedelta(days=days_to_subtract))        
            current_week_start = new_time.strftime('%Y-%m-%d 00:00:00')                 
        case "Saturday":
            current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            days_to_subtract = 0
            new_time = (current_time - datetime.timedelta(days=days_to_subtract))
            current_week_start = new_time.strftime('%Y-%m-%d 00:00:00')         
        
        case "Sunday":
            current_time = datetime.datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            days_to_subtract = 1
            new_time = (current_time - datetime.timedelta(days=days_to_subtract))
            current_week_start = new_time.strftime('%Y-%m-%d 00:00:00') #the beginning of the current week         


    next_week = (new_time - datetime.timedelta(days=-6))
    current_week_end = next_week.strftime('%Y-%m-%d 23:59:59') #the ending of the current week       

    results = []
    results.append(current_week_start)
    results.append(current_week_end)
    return(results)


print('The beginning of the current week is: ', current_week_calculator()[0])
print('The ending of the current week is: ', current_week_calculator()[1])

