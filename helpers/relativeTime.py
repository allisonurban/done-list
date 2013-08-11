import datetime 

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
this_week = today - datetime.timedelta(days=today.weekday())
last_week_start = today - datetime.timedelta(days=today.weekday(), weeks=1)
last_week_end = last_week_start + datetime.timedelta(weeks=1)

# this week
# get date of first day of this week




print today
print yesterday
print this_week
print last_week_start
print last_week_end

# today
# yesterday
# this week
# last week
# this month
# last month
# since last week
# 1.days.ago
# 7.days.ago
# 1.month.ago