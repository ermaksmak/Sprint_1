def run1():
    time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
    total_minutes = 0
    print('time_string = ',time_string," total_minutes = ",total_minutes)

    time_values = time_string.split(',')
    for time_value in time_values:
        time_value = time_value.replace(' ', '')
        if 'h' in time_value:
            hours = int(time_value.split('h')[0])
            total_minutes += hours * 60
            time_value = time_value.split('h')[1]
        if 'm' in time_value:
            minutes = int(time_value.split('m')[0])
            total_minutes += minutes
            time_value = time_value.split('m')[1]
        if 's' in time_value:
            seconds = int(time_value.split('s')[0])
            total_minutes += seconds // 60
    print(f'total_minutes_after_convert: {total_minutes}')