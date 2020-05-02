'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

distance_miles = 10
distance_km = distance_miles*1.6

time_minutes = 30
time_seconds = 30
time_hours = (time_minutes/60) + ((time_seconds/60)/60)

average_speed = distance_km/time_hours

print(str(average_speed) + " km/h")