# daily_challenges/day01_greeting.py
# Day 1 — Greeting Generator (manual time-of-day version)
# (next upgrade): input validation

name = input("Hello there! Please enter your name: ").strip().title()


while True:
    time_of_day = input("What part of the day is it? (Time for ex: 7pm): ").strip().lower()

    # Validate suffix
    if not (time_of_day.endswith("am") or time_of_day.endswith("pm")):
        print(f"{name}, Invalid format! Please enter a time like '7am' or '11pm'.")
        continue

    # Separating each string parts
    hour_str = time_of_day[:-2]
    suffix = time_of_day[-2:]

    # Validation of the numeric part
    if not hour_str.isdigit():
        print(f"{name}, invalid hour! Please enter a number followed by am/pm (e.g., 7am, 11pm).")
        continue

    hour = int(hour_str) # transform string to int

    if hour < 1 or hour > 12:
        print(f"{name}, the hour must be between 1 and 12. Please try again, my love")
        continue

    if suffix == "pm" and hour != 12:
        hour += 12 # if it is 12pm, leave as is. If it's 1pm onwards, then add 12 so it's 13, 14 etc
    elif suffix == "am" and hour == 12:
        hour = 0 # to handle midnight hour

    break

if hour >= 0 and hour < 12:
    greeting = f"Good morning, {name}! I hope you have a wonderful day ahead of you 💗"
elif hour >= 12 and hour < 18:
    greeting = f"Good afternoon, {name}! Enjoy your lunch, don't forget to take a break 😋"
elif hour >= 18 and hour < 24:
    greeting = f"Good evening, {name}! Hope your day went well 💓"
else:
    # Fallback for a mistake
    greeting = f"Hello, {name}! You may have made a mistake in your time input! Try again "

print(greeting)
