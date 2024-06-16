def is_magic_date(day, month, year):
    return day * month == int(str(year)[-2:])

def find_magic_dates():
    magic_dates = []
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                if day * month == int(str(year)[-2:]):
                    magic_dates.append(f"{month}/{day}/{year}")
    return magic_dates


magic_dates_20th_century = find_magic_dates()
for date in magic_dates_20th_century:
    print(date)
