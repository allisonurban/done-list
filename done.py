import csv
#from time import localtime, strftime
import datetime 
from optparse import OptionParser

def get_date_time():
	# return strftime("%Y-%m-%d, %I:%M%p", localtime())
	return datetime.datetime.now()

def load_tasks(filename="done.csv"):
	r = csv.reader(open(filename))
	tasks = {}
	for task in r:
		tasks[task[0]] = task[1]
	return tasks

def save_task(task, filename="done.csv"):
	date_time = get_date_time()
	print date_time
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
		today = datetime.date.today().strftime("%Y-%m-%d")
		yesterday = datetime.date.today()-datetime.timedelta(days=1)
		# TODO: add error handling for no arguments

		if args[0].lower() == "today":

			for date,task in done_list.iteritems():
				if date >= today:
					print task
		elif args[0].lower() == "yesterday":
			
			for date,task in done_list.iteritems():
				if date < today and date >= yesterday.strftime("%Y-%m-%d"):
					print task
		else:
			for date,task in done_list.iteritems():
				print date,task

		

