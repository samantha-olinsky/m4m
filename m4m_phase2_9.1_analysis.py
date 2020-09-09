import json
import datetime
import csv

with open("meal4monsters-export_v8.1.json", "r") as read_file:
    data = json.load(read_file)  


users = [ 

"ID-0812-125410AMBRT-93573122",
## below is converted Korean entry
"ID-0812-072424pmGMT+02:00-453167386",
"ID-0813-025640PMEDT-98934737",
"ID-0813-040151PMGMT-03:00-948836545",
"ID-0813-102021PMIST-460234729",
"ID-0813-102401pmGMT+05:30-680725392",
"ID-0813-103623PMGMT+05:30-673506994",
"ID-0813-103951PMGMT+05:30-489846797",
"ID-0813-105633PMCDT-380564685",
"ID-0813-110353pmGMT+05:30-903135320",
"ID-0813-110809pmGMT+05:30-924446122",
"ID-0814-011843amGMT+05:30-774901885",
"ID-0814-013456AMGMT+05:30-768567456",
"ID-0814-034808PMEDT-396238958",
"ID-0814-082119amGMT+05:30-460761561",
"ID-0814-102512PMEDT-941428973",
"ID-0815-021205AMIST-931241271",
"ID-0815-123523AMIST-144841739",
"ID-0818-085456PMEDT-127206547",
"ID-0820-061851PMEST-858229596",
"ID-0820-094820AMCDT-334550354",
"ID-0820-103441pmGMT+05:30-107565429",
"ID-0825-062237PMBRT-570410986",
"ID-0825-071923PMPDT-482888411",
"ID-0826-014959amGMT+05:30-208802805",
"ID-0826-020443AMIST-881688",
"ID-0826-034143AMGMT+05:30-527841283",
"ID-0826-042232pmGMT+05:30-111992536",
"ID-0826-042738AMGMT+05:30-508328457",
"ID-0826-095243amGMT+05:30-328382904",
"ID-0830-054520PMCDT-2898864",
"ID-0830-103515pmGMT+05:30-620306760",
"ID-0830-084718PMIST-679108612",
"ID-0830-043845pmCEST-88243611",
"ID-0830-023422PMCDT-247099562",
"ID-0811-010005AMGMT+02:00-98573590",
"ID-0811-020929PMEDT-898995352",
"ID-0811-062108PMGMT+02:00-686600640",
"ID-0811-102657PMEDT-792152583",
"ID-0811-122926PMCDT-406797805",
"ID-0812-071209AMBRT-39677090",
"ID-0812-073905PMBRT-685184568",
"ID-0812-074923PMBRT-592296978",
"ID-0812-101304AMBRT-848432031",
"ID-0812-120315AMBRT-845270635",
"ID-0812-120827AMBRT-310871708",
"ID-0812-123833AMBRT-266191036",
"ID-0813-062558PMEDT-774714436",
"ID-0813-033201PMEDT-111908228",
"ID-0813-073121PMCDT-707321989",
"ID-0814-060649PMGMT+02:00-806874326",
"ID-0814-061401PMEDT-799736227",
"ID-0814-061529PMEDT-985247169",
"ID-0814-084759PMPDT-830987008",
"ID-0814-124259PMEDT-510802953",
"ID-0815-031345PMEDT-186461766",
"ID-0815-032743AMIST-703379681",
"ID-0816-084851AMEDT-255935211",
"ID-0816-114356AMEDT-489059163",
"ID-0816-114536AMEDT-374674448",
"ID-0817-014501pmCEST-630779850",
"ID-0817-044223PMEDT-815539722",
"ID-0818-100221AMEDT-592049191",
"ID-0818-112940AMEDT-618142101",
"ID-0819-100243amCEST-351690746",
"ID-0822-010948AMGMT+05:30-880630879",
"ID-0822-105045AMEDT-341496192",
"ID-0826-124603PMIST-530874004"
]


def getOrderOfRounds(dict):
	roundLetters = []
	for x in xrange(1,6):
		for field in dict:
			if (field[8] == str(x)):
				roundLetters.append(field[6])
				break
	return roundLetters

roundInfoAMT = [ ]
for item in users:
	for userRnd in data["M4M_Phase2_AMT"]: 
		if (item == userRnd):
			letters = getOrderOfRounds(data["M4M_Phase2_AMT"][userRnd])	
			print(userRnd + ", " + ", ".join(letters))
print (roundInfoAMT)

roundInfoSM = [ ]
for item in users:
	for userRnd in data["M4M_Phase2_SM"]: 
	
		if (item == userRnd):
			letters = getOrderOfRounds(data["M4M_Phase2_SM"][userRnd])	
			print(userRnd + ", " + ", ".join(letters))
#print (roundInfoSM)
#print (len(users))




#### CARROED OVER FROM PHASE1 CODE
#### LET'S SEE how much can be re-used


newL = [ ]  
for item in users:
			
			#print(type(userRnd))
	for userRnd in data["M4M_Phase2_AMT"]:
		if (item == userRnd):
			userValue = data["M4M_Phase2_AMT"][userRnd]  
			newL.append(   (userRnd , userValue) )

	for userRnd in data["M4M_Phase2_SM"]:
		if (item == userRnd):
			userValue = data["M4M_Phase2_SM"][userRnd]  
			newL.append(   (userRnd , userValue) )


#print (newL)

newDict = dict(newL)

def readTimestamp(timestamp):
	return datetime.datetime.strptime(timestamp, '%m %d %Y_%H %M %S %p') 


def getRoundTime(user,whichRound):
	ts = dict(newL)[user]["timestamps"]
	rnd = dict(newL)[user] ## this basically has everything from firebase except the assigned monster number and the userID itself. 
	startTime = ""
	endTime = ""
	total_Dur=""
	#timestamps are keys, events are values
	#print(whichRound + "!")
	for key in sorted(ts):

		#if (not startTime == "") and (endTime == "") and (ts[key].endswith("begins\"") or ts[key]=="\"Game Result\""): 
		if (not startTime == "") and (endTime == "") and (ts[key]=="\"Game Result\""): 
			endTime = key
			#print("t")
			#print ("Start Time: " + startTime) 
		if ts[key] == "\"round "+whichRound+" begins\"":
			startTime = key
			#print ("End Time: " + endTime) ----- THIS HAS NEVER PRINTED PROPERLY
	if (not startTime == "") and (not endTime == ""):
		total_Dur = (str(readTimestamp(endTime) - readTimestamp(startTime)))
		print ("First Rnd to Game Result Duration: " + str(readTimestamp(endTime) - readTimestamp(startTime)))
	#print (rnd)	

# 	### this is where I will start the duration the users spent on the community board page in each round
# 	### so there is (if collected properly), five duration instances (each one for each round) per user
# 	## so from "reason submit button click" to "comm submit button click" per each round OR after the first round up to "round # result screen"

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
	#print (count_array)
	freq_clicks_array = count_array
	# print ("Community Board Round A Clicks: " + str(count_array[0]))	
	# print ("Community Board Round B Clicks: " + str(count_array[1]))	
	# print ("Community Board Round C Clicks: " + str(count_array[2]))	
	# print ("Community Board Round D Clicks: " + str(count_array[3]))	
	# print ("Community Board Round E Clicks: " + str(count_array[4]))
	
	cb_1_clicks = str(count_array[0])
	cb_2_clicks = str(count_array[1])
	cb_3_clicks = str(count_array[2])
	cb_4_clicks = str(count_array[3])
	cb_5_clicks = str(count_array[4])





	rnd1_d = readTimestamp(rnd1_result) - readTimestamp(startTime) 
	rnd2_d = readTimestamp(rnd2_result) - readTimestamp(rnd1_result) 
	rnd3_d = readTimestamp(rnd3_result) - readTimestamp(rnd2_result) 
	rnd4_d = readTimestamp(rnd4_result) - readTimestamp(rnd3_result) 
	rnd5_d = readTimestamp(rnd5_result) - readTimestamp(rnd4_result) 

	# print("Round A Duration: " + str(rnd1_d))
	# print("Round B Duration: " + str(rnd2_d))
	# print("Round C Duration: " + str(rnd3_d))
	# print("Round D Duration: " + str(rnd4_d))
	# print("Round E Duration: " + str(rnd5_d))

	rnd1_dur = str(rnd1_d)
	rnd2_dur = str(rnd2_d)
	rnd3_dur = str(rnd3_d)
	rnd4_dur = str(rnd4_d)
	rnd5_dur = str(rnd5_d)


 	init_choice = {} 
 	comm_choice = {} 
	## initialize them as an empty dictionary and then read them when I am done with the loop

	#round_L-#_choice/reason : keys
	#numbers (specifically #-#) and reasonings in text: values
	initial_choices = [ ]
	initial_reasons = [ ]
	initial_reasons_len = [ ]
	community_choices = [ ]
	community_reasons = [ ]
	community_reasons_len = [ ]

	rnd1_preCB_Correct = [ ]
	rnd1_postCB_Correct = [ ]
	rnd5_preCB_Correct = [ ]
	rnd5_postCB_Correct = [ ]
	
	rnd_Correct = [ ]

	for key in sorted(rnd):	
		mealShown = key[8]  ## this is the number after the letter:  B-5 (the number of that format)????
		letter = key[6] ## this is the letter before the number: B-5 (the letter of that format)????
		reason = rnd[key]


		if (key.endswith("t_choice")):
			init_choice[str(mealShown)] = rnd[key][1]
			#print ("Round " + mealShown + " Choice: " + reason[1])
			#print ("Round Letter: " + letter)
			initial_choices.append(reason[1])
			
			if (reason[1]=="1"):
				#print ("Round 1 correct: YES" )
				rnd_Correct.append(1)
				#print (rnd_Correct)
			else:
				#print ("incorrect")
				rnd_Correct.append(0)


		if (key.endswith("t_reason")):
			print ("Round " + mealShown + " Reason: " + reason) 	
			initial_reasons.append(reason)
			initial_reasons_len.append(len(reason))
			#print ("Round " + mealShown + " Reason length: " + len(reason))
			

		if (key.endswith("m_choice")):
			comm_choice[str(mealShown)] = rnd[key]		
			#print ("Round " + mealShown + " Post-Community Choice: " + reason)
			community_choices.append(reason)

		if (key.endswith("m_reason")):
			print ("Round " + mealShown + " Post-Comm Reason: " + reason) 
			#print (mealShown)
			community_reasons.append(reason)
			community_reasons_len.append(len(reason))


	#print (rnd_Correct)	
	print (initial_reasons_len)
	print (community_reasons_len)  ### only about 10 ppl were after the code was corrected and pre-CB and post-CB are actually different. 



	## checking if the choices the user selected were correct '1' or incorrect '2', '3', or '4' in Round 1	
	for number in initial_choices:
		if number == "1":
			rnd1_preCB_Correct.append(1)
			#print (rnd1_preCB_Correct)
		else: 
			rnd1_preCB_Correct.append(0)

	for number in community_choices:
		if number == "1":
			rnd1_postCB_Correct.append(1)
		else: 
			rnd1_postCB_Correct.append(0)

	for number in initial_choices:
		if number == "1":
			rnd5_preCB_Correct.append(1)
		else: 
			rnd5_preCB_Correct.append(0)

	for number in community_choices:
		if number == "1":
			rnd5_postCB_Correct.append(1)
		else: 
			rnd5_postCB_Correct.append(0)


	answer_changes = [ ]
	#answer_not_change = [ ]
	for x in xrange(1,6):
		if (init_choice[str(x)] == comm_choice[str(x)]):
			#print ("Round " + str(x) + " Answer Change: 1") ## meal choice REMAINED THE SAME
			answer_changes.append(1) 

		else:
			#print ("Round " + str(x) + " Answer Change: 0") ## meal choice changed after community board
			answer_changes.append(0)





	
	return { "total duration": total_Dur, "frequency clicks all": freq_clicks_array, "community 1 clicks": cb_1_clicks, "community 2 clicks": cb_2_clicks,
			"community 3 clicks": cb_3_clicks, "community 4 clicks": cb_4_clicks, "community 5 clicks": cb_5_clicks, "round 1 duration": rnd1_dur, "round 2 duration": rnd2_dur, "round 3 duration": rnd3_dur, 
			"round 4 duration": rnd4_dur, "round 5 duration": rnd5_dur, 
			"initial choices": initial_choices,
			"initial reasons": initial_reasons, 
			"initial length":initial_reasons_len,
			"comm choices": community_choices, 
			"comm reasons": community_reasons, 
			"comm length":community_reasons_len,
			"answer change": answer_changes,
			"Rnd1_preCB_Correct": rnd1_preCB_Correct, 
			"Rnd1_postCB_Correct": rnd1_postCB_Correct,
			"Rnd5_preCB_Correct": rnd5_preCB_Correct, 
			"Rnd5_postCB_Correct": rnd5_postCB_Correct,
			"Rnd_Correctness": rnd_Correct 
			}

def firstLetter(ts):
	
	for t in sorted(ts):
		if ( ts[t].startswith("\"round ") and ts[t].endswith("begins\"")  ) : ## believe this is getting the B, D, A, E, C letters under "timestamps"
			return ts[t][7]
	print("didnt find a letter!")
	exit(1)

for user, userData in newL: 
	try:
		print ("Monster Choice: " + newDict[user]["monster choice"])
		newDict[user]["results"] = getRoundTime(user,firstLetter(newDict[user]["timestamps"])) 
		print ("")
	except Exception as ex:
	    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
	    message = template.format(type(ex).__name__, ex.args)
	    print message
#print (newDict[user]["results"])



with open('m4m_phase2_len.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["userID", "condition", "Monster_Number", "len1", "len2", "len3", "len4", "len5", "all_initial_len", "len1_1", "len1_2", "len1_3", "len1_4", "len1_5", "all_comm_len"])

    for row, userData in newL:
    	try:
    		writer.writerow([ 
    		#userIDs
    		row, "1", newDict[row]["monster choice"], 
    		#length of the initial reasons pre-CB
    		newDict[row]["results"]["initial length"][0],
    		newDict[row]["results"]["initial length"][1],
    		newDict[row]["results"]["initial length"][2],
    		newDict[row]["results"]["initial length"][3],
    		newDict[row]["results"]["initial length"][4],

    		(newDict[row]["results"]["initial length"][0] +
    		newDict[row]["results"]["initial length"][1] +
    		newDict[row]["results"]["initial length"][2] +
    		newDict[row]["results"]["initial length"][3] +
    		newDict[row]["results"]["initial length"][4]),

    		newDict[row]["results"]["comm length"][0],
    		newDict[row]["results"]["comm length"][1],
    		newDict[row]["results"]["comm length"][2],
    		newDict[row]["results"]["comm length"][3],
    		newDict[row]["results"]["comm length"][4],

    		(newDict[row]["results"]["comm length"][0] +
    		newDict[row]["results"]["comm length"][1] +
    		newDict[row]["results"]["comm length"][2] +
    		newDict[row]["results"]["comm length"][3] +
    		newDict[row]["results"]["comm length"][4])
    		])
    		
    	except Exception as e:
    		print (e)
################################################################################################################################################################################
###################### THE COLUMNS IN CSV RIGHT NOW AS IT Is BELOW wiLL NOT MATch the results above as another column or so has been added. 
##########################################################################################################################################################

# with open('m4m_phase2_analysis.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["userID","Monster_Number","First_Rnd_to_Game_Result_Duration",
#     	"Rnd1_Duration","Rnd2_Duration","Rnd3_Duration","Rnd4_Duration","Rnd5_Duration",
#     	"Init_Choice1","Init_Reason1",
#     	"Init_Choice2","Init_Reason2",
#     	"Init_Choice3","Init_Reason3",
#     	"Init_Choice4","Init_Reason4",
#     	"Init_Choice5","Init_Reason5",
#     	"Rnd1_Correct", "Rnd2_Correct","Rnd3_Correct", "Rnd4_Correct", "Rnd5_Correct"])
#     for row, userData in newL:
#     	try:
#     		writer.writerow([ 
#     		#userIDs
#     		row, newDict[row]["assigned_monster_num"],
#     		# total duration of the five rounds
#     		newDict[row]["results"]["total duration"],

#     		## durations in order of rounds per round
#     		newDict[row]["results"]["round 1 duration"],newDict[row]["results"]["round 2 duration"],newDict[row]["results"]["round 3 duration"],
#     		newDict[row]["results"]["round 4 duration"],newDict[row]["results"]["round 5 duration"],
    		
#     		#round 1 -- choices and reasons
#     		newDict[row]["results"]["User_choices"][0],newDict[row]["results"]["User_reasons"][0],
#     		#round 2 -- choices and reasons
#     		newDict[row]["results"]["User_choices"][1],newDict[row]["results"]["User_reasons"][1],
#     		#round 3 -- choices and reasons
#     		newDict[row]["results"]["User_choices"][2],newDict[row]["results"]["User_reasons"][2],
#     		#round 4 -- choices and reasons
#     		newDict[row]["results"]["User_choices"][3],newDict[row]["results"]["User_reasons"][3],
#     		#round 5 -- choices and reasons
#     		newDict[row]["results"]["User_choices"][4],newDict[row]["results"]["User_reasons"][4],


#     		#correctness of meal choices per round
#     		newDict[row]["results"]["Rnd_Correctness"][0], 
#     		#initial choices in Round 5
# 			newDict[row]["results"]["Rnd_Correctness"][1],
#     		#post CB choices in Round 1
# 			newDict[row]["results"]["Rnd_Correctness"][2],
#     		#post CB choices in Round 5
# 			newDict[row]["results"]["Rnd_Correctness"][3],
# 			#post CB choices in Round 5
# 			newDict[row]["results"]["Rnd_Correctness"][4]
#     			])
#     	except Exception as e:
#     		print (e)

print (len(newL))


























