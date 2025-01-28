from datetime import datetime, timedelta

def str_to_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def is_conflicting(event1, event2):
    return (str_to_time(event1['start']) < str_to_time(event2['end']) and 
            str_to_time(event1['end']) > str_to_time(event2['start']))

schedule = [
    {"name": "Meeting A", "start": "09:00", "end": "10:30"},
    {"name": "Workshop B", "start": "10:00", "end": "11:30"},
    {"name": "Presentation C", "start": "10:30", "end": "12:00"},
    {"name": "Lunch Break", "start": "12:00", "end": "13:00"},
]

sorted_schedule = sorted(schedule, key=lambda event: str_to_time(event['start']))

print("Sorted Schedule:")
for i, event in enumerate(sorted_schedule, start=1):
    print(f'{i}. "{event["name"]}", Start: "{event["start"]}", End: "{event["end"]}"')

conflicts = []
for i in range(len(sorted_schedule) - 1):
    if is_conflicting(sorted_schedule[i], sorted_schedule[i+1]):
        conflicts.append((sorted_schedule[i], sorted_schedule[i+1]))

if conflicts:
    print("\nConflicting Events:")
    for i, conflict in enumerate(conflicts, start=1):
        print(f'{i}. "{conflict[0]["name"]}" and "{conflict[1]["name"]}"')

if conflicts:
    print("\nSuggested Resolutions:")

    event_to_reschedule = conflicts[0][1]
    suggested_start = str_to_time("13:00").strftime("%H:%M")  
    suggested_end = (str_to_time(suggested_start) + timedelta(hours=1, minutes=30)).strftime("%H:%M")  
    print(f'1. Reschedule "{event_to_reschedule["name"]}" to Start: "{suggested_start}", End: "{suggested_end}"')
