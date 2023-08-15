def add_time(start, duration, day=None):
    start_time, meridiem = start.split()
    start_hr, start_min = map(int, start_time.split(":"))
    duration_hr, duration_min = map(int, duration.split(":"))

    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    days_later = 0
    minutes = start_min + duration_min
    hours = start_hr + duration_hr

    if minutes >= 60:
        hours += 1
        minutes -= 60

    meridiem_cycles = hours // 12
    hours = hours % 12

    # taking mod of hours can return 00, so we fix for 12-hour clock format
    hours = hours = 12 if hours == 0 else hours

    # if num of cycles is even we are staying AM -> AM or PM -> PM, if it's odd we are changing AM -> PM or PM -> AM
    if meridiem_cycles % 2 == 1:
        if meridiem == "PM":
            meridiem = "AM"

            # adding 1 compensates for day change even when start-time is PM and added-time < 12, ex: 6:58pm + 8:12
            days_later = (1 + meridiem_cycles) // 2
        else:
            meridiem = "PM"
            days_later = meridiem_cycles // 2
    else:
        days_later = meridiem_cycles // 2

    # format start of string, pad minutes to appear as 00...09
    new_time = f"{hours}:{minutes:02d} {meridiem}"

    # optional day arg passed, convert text to "Capitalized" format with .title()
    # index start_day pos, add num of days passed and take the mod of new "index" to return valid value in list
    if day:
        start_day = days_of_week.index(day.title())
        new_day = int((start_day + days_later) % 7)
        new_time += f", {days_of_week[new_day]}"

    # if next day or more, append appropriate text
    if days_later == 1:
        new_time += f" (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
