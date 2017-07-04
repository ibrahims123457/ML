def formatDateTime(dateTime):
    array = dateTime.split(' ')

    # date
    array[0] = array[0].split('/')  # split into month, date, year

    if len(array[0][0]) == 1:   # if month is single digit, add 0 in front
        array[0][0] = '0' + array[0][0]

    if len(array[0][1]) == 1:   # if day is single digit, add 0 in front
        array[0][1] = '0' + array[0][1]

    date = array[0][2] + '-' + array[0][0] + '-' + array[0][1]   # proper numpy date format

    # time
    array[2] = array[2].split(':')  # split into hour, minute, second
    if len(array[2][0]) == 1:   # if the hour is single digit, add 0 in front
        array[2][0] = '0' + array[2][0]
    time = array[2][0] + ':' + array[2][1] + ':' + array[2][2]  # put back into string
    
    #check if AM or PM
    if array[3] == 'AM':
        return np.datetime64(date + 'T' + time)
    return np.datetime64(date + 'T' + time) + np.timedelta64(12, 'h')