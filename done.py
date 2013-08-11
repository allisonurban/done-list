import csv
import datetime 
from optparse import OptionParser
# import bettertime

def get_date_time():
	return datetime.datetime.today()

def load_tasks(filename="done.csv"):
	r = csv.reader(open(filename))
	tasks = {}
	for task in r:
		tasks[task[0]] = task[1]
	return tasks

def save_task(task, filename="done.csv"):
	date_time = get_date_time()
	with open(filename, 'ab') as csvfile:
		w = csv.writer(csvfile)
		w.writerow([date_time,task])


if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-a", "--add", dest="add", action="store_true")
	(options, args) = parser.parse_args()

	if options.add: # we're adding a new task
		save_task(args[0])

	else: # print out what was done
		done_list = load_tasks()
		timeframe = "".join(args).lower()
		today = datetime.date.today()

		# today = datetime.date.today().strftime("%Y-%m-%d")
		# yesterday = datetime.date.today()-datetime.timedelta(days=1)
		# TODO: add error handling for no arguments

		for date,task in done_list.iteritems():
			task_date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").date()

			if timeframe == "today" and task_date == today:
					print task
			elif timeframe == "yesterday" and task_date == today - datetime.timedelta(days=1):
					print task
			elif timeframe == "thisweek" and task_date > today  and task_date < today - datetime.timedelta(days=today.weekday(), weeks=1):
					print task





