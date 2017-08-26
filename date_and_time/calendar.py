import calendar

if __name__ == "__main__":
    month, day, year = map(int, raw_input().split())
    days = map(str.upper,list(calendar.day_name))
    print days[calendar.weekday(year, month, day)]
