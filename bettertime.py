

def get_date_time():

	# my_datetime_obj = datetime.datetime.now()
	# print type(my_datetime_obj)
	# print type(my_datetime_obj.date())
	# print type(my_datetime_obj.time())
						
	print datetime.datetime.now()											# 2013-08-10 23:05:26.702795 	<type 'datetime.datetime'>
	print datetime.datetime.now().date()							# 2013-08-10									<type 'datetime.date'>
	print datetime.datetime.now().time()							# 23:10:11.969733							<type 'datetime.time'>
										
	print datetime.datetime.today()										# 2013-08-10 23:05:26.702795	<type 'datetime.datetime'>
	print datetime.datetime.today().date()						# 2013-08-10									<type 'datetime.date'>
	print datetime.datetime.today().time()						# 23:10:11.969733							<type 'datetime.time'>

	print datetime.date.today()												# 2013-08-10									<type 'datetime.date'>
	print datetime.time()															# 00:00:00 										<type 'datetime.time'>

	print datetime.timedelta(days=1)									# 1 day, 0:00:00 							<type 'datetime.timedelta'>
	print datetime.date.today() - datetime.timedelta(days=1)	# 2013-08-09		<type 'datetime.date'>


get_date_time()
