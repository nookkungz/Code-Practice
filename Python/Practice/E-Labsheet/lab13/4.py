start = input()
end = input()
f = int(input())

start_day = int(start[0:2])
start_month = int(start[3:5])
end_day = int(end[0:2])
end_month = int(end[3:5])

wrong_month = False
wrong_day = False

if start_month < 1 or start_month > 12:
    wrong_month = True
if end_month < 1 or end_month > 12:
    wrong_month = True

if start_month == 2:
    if start_day < 1 or start_day > 28:
        wrong_day = True
if start_month in [4, 6, 9, 11]:
    if start_day < 1 or start_day > 30:
        wrong_day = True
if start_day < 1 or start_day > 31:
    wrong_day = True

if end_month == 2:
    if end_day < 1 or end_day > 28:
        wrong_day = True
if end_month in [4, 6, 9, 11]:
    if end_day < 1 or end_day > 30:
        wrong_day = True
if end_day < 1 or end_day > 31:
    wrong_day = True

if wrong_month:
    print("Wrong Month")
if wrong_day:
    print("Wrong Day")

if not wrong_month and not wrong_day:
    sundays = 0
    current_day = 1
    current_month = 1
    current_weekday = f

    days_in_month = [31, 30, 31, 31, 30, 31, 30, 31, 30, 31, 30, 31]

    while (current_month < start_month) or (current_month == start_month and current_day < start_day):
        current_day += 1
        current_weekday = (current_weekday + 1) % 7
        if current_day > days_in_month[current_month - 1]:
            current_day = 1
            current_month += 1

    while (current_month < end_month) or (current_month == end_month and current_day <= end_day):
        if current_weekday == 0:
            sundays += 1
        current_day += 1
        current_weekday = (current_weekday + 1) % 7
        if current_day > days_in_month[current_month - 1]:
            current_day = 1
            current_month += 1

    print(sundays)