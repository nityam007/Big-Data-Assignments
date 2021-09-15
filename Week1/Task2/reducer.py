#!/usr/bin/env python3
 
import sys
import simplejson as json
 
current_state = None
current_city = None
current_count = 0
for line in sys.stdin:
	# line = line.strip()
	# print(line)
	state, city, temp_count = line.split('$')
	count = int(temp_count)
	# print(state, city, count)

	if current_state == state:
		if current_city == city:
			current_count +=count
		
		else :
			print(current_city,current_count)
			current_city=city
			current_count=count
	else:
		print(state)
		current_state=state
		current_city=city
		current_count=count
