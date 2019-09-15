def get_time_intervals(start, end, interval):
    intervals=[]
    current_time=start
    while current_time + interval < end :
        intervals.append((current_time,current_time + interval))
    return intervals