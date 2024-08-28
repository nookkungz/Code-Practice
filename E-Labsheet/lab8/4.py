

def read_hour() :
    h = int(input("Enter hour: "))
    return h

def read_minute () :
    m = int(input("Enter minute: "))
    return m

def read_second() :
    s = int(input("Enter second: "))
    return s

def to_seconds(h,m,s):
    result =  ((h*60)*60) + m*60 + s
    return result

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

def time_elapsed (start , finish) :
    result = finish - start
    hour , min = 0 , 0
    if result // 3600 >= 1 :
        hour = (result // 3600)
        result -= (result // 3600)*3600
    if result // 60 >= 1 :
        min = (result // 60)
        result -= (result // 60)*60
    done = f"{hour} hours {min} minutes {result} seconds."
    return done




print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))