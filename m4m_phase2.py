import json
import datetime
import csv

with open("meal4monsters-export_v2.2.json", "r") as read_file:
    data = json.load(read_file)  
    ## Note that I took out one data entry from the JSON file bc the one with Korean in it is not ascii and was
    ## throwing errors. So that one Korean entry (userID that includes Korean) will have to added manually.



def readTimestamp(timestamp):
	return datetime.datetime.strptime(timestamp, '%m %d %Y_%H %M %S %p') 
	### how we are (if at all) mediating for the fact that time is recorded
	### in the time zone the device is set to. Therefore, we have GMT, EST, CDT, etc.
	### Since we are only recording the time difference we do NOT have to worry about this issue. 

def getRoundTime(user,whichRound):
	ts = data["M4M_Phase2_SM"][user]["timestamps"]
	rnd = data["M4M_Phase2_SM"][user]
	startTime = ""
	endTime = ""

	#timestamps are keys, events are values
	for key in sorted(ts):
		#if (not startTime == "") and (endTime == "") and (ts[key].endswith("begins\"") or ts[key]=="\"Game Result\""): 
		if (not startTime == "") and (endTime == "") and (ts[key]=="\"Game Result\""): 
			endTime = key
			#print ("Start Time: " + startTime) 
		if ts[key] == "\"round "+whichRound+" begins\"":
			startTime = key
	if (not startTime == "") and (not endTime == ""):
		total_Dur = (str(readTimestamp(endTime) - readTimestamp(startTime)))
		#print ("Round A to Game Result Duration: " + str(readTimestamp(endTime) - readTimestamp(startTime)))
	

	### this is where I will start the duration the users spent on the community board page in each round
	### so there is (if collected properly), five duration instances (each one for each round) per user
	## so from "reason submit button click" to "comm submit button click" per each round OR after the first round up to "round # result screen"

	for key in sorted(ts):
		if ts[key] == "\"reason submit button click\"":
			startTime = key
			break #break here

	for key in sorted(ts):
		if ts[key] == "\"round 1 result screen\"":
			rnd1_result = key
		if ts[key] == "\"round 2 result screen\"":
			rnd2_result = key
		if ts[key] == "\"round 3 result screen\"":
			rnd3_result = key
		if ts[key] == "\"round 4 result screen\"":
			rnd4_result = key
		if ts[key] == "\"round 5 result screen\"":
			rnd5_result = key

	counter=0
	count_array = []

	
	for key in sorted(ts):
		counter +=1
		if ts[key] == "\"reason submit button click\"":
			counter = 0 	
		if ts[key] == "\"comm submit button click\"":
			count_array.append(counter)
	print (count_array)
	print ("Community Board Round A Clicks: " + str(count_array[0]))
	print ("Community Board Round B Clicks: " + str(count_array[1]))
	print ("Community Board Round C Clicks: " + str(count_array[2]))
	print ("Community Board Round D Clicks: " + str(count_array[3]))
	print ("Community Board Round E Clicks: " + str(count_array[4]))



	rnd1_d = readTimestamp(rnd1_result) - readTimestamp(startTime) 
	rnd2_d = readTimestamp(rnd2_result) - readTimestamp(rnd1_result) 
	rnd3_d = readTimestamp(rnd3_result) - readTimestamp(rnd2_result) 
	rnd4_d = readTimestamp(rnd4_result) - readTimestamp(rnd3_result) 
	rnd5_d = readTimestamp(rnd5_result) - readTimestamp(rnd4_result) 

	print("Round A Duration: " + str(rnd1_d))
	print("Round B Duration: " + str(rnd2_d))
	print("Round C Duration: " + str(rnd3_d))
	print("Round D Duration: " + str(rnd4_d))
	print("Round E Duration: " + str(rnd5_d))




	init_choice = {} 
	comm_choice = {} 
	## initialize them as an empty dictionary and then read them when I am done with the loop

	#round_L-#_choice/reason : keys
	#numbers (specifically #-#) and reasonings in text: values
	for key in sorted(rnd):	
		mealShown = key[8]
		reason = rnd[key]


		if (key.endswith("t_choice")):
			init_choice[str(mealShown)] = rnd[key][1]
			print ("Round " + mealShown + " Initial Choice: " + reason[1])
		
		if (key.endswith("t_reason")):
			print ("Round " + mealShown + " Initial Reason: " + reason) 	
			
		if (key.endswith("m_choice")):
			comm_choice[str(mealShown)] = rnd[key]		
			print ("Round " + mealShown + " Post-Community Choice: " + reason)

		if (key.endswith("m_reason")):
			print ("Round " + mealShown + " Post-Comm Reason: " + reason) 
			#print (mealShown)
		
	for x in xrange(1,6):
		if (init_choice[str(x)] == comm_choice[str(x)]):
			print ("Round " + str(x) + " Answer Change: 1") ## meal choice REMAINED THE SAME
		else:
			print ("Round " + str(x) + " Answer Change: 0") ## meal choice changed after community board
				


for user in data["M4M_Phase2_SM"]: 
	print (user)
	try:
		print ("Monster Choice: " + data["M4M_Phase2_SM"][user]["monster choice"])
		getRoundTime(user,"A") ## getRoundTime's function second argument is "A", 
		#the problem is for some users whichRound did not always start with A for whatever reason/bug.
		print ("")
	except Exception as e:
		print (e)
		print ("")

with open('m4m.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["userID","Monster_Number","RndA to Game Result Duration","Community Board Freq Clicks Array","CB Clicks A","CB Clicks B","CB Clicks C","CB Clicks D","CB Clicks E","RndA Duration","RndB Duration","RndC Duration","RndD Duration","RndE Duration","Init Choice","Init Reason","Community Choice","Community Reason","Init Choice","Init Reason","Community Choice","Community Reason","Init Choice","Init Reason","Community Choice","Community Reason","Init Choice","Init Reason","Community Choice","Community Reason","Init Choice","Init Reason","Community Choice","Community Reason","Rnd1 Answer Change","Rnd2 Answer Change","Rnd3 Answer Change","Rnd4 Answer Change","Rnd5 Answer Change" ])
    for row in data["M4M_Phase2_SM"]:
    	try:
    		writer.writerow([ row, data["M4M_Phase2_SM"][row]["monster choice"]   ])
    	except Exception as e:
    		pass

