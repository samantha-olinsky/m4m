import json
import datetime
import csv

with open("meal4monsters-export_v6.1.json", "r") as read_file:
    data = json.load(read_file)  

users = [ 

"ID-0611-104949AMIST-330607551",
"ID-0611-111059amIST-584611746",
"ID-0609-121243amGMT+05:30-911033927",
"ID-850716044-085459",
"ID-500495237-073714",
"ID-0608-021856PMEDT-720575577",
"ID-0611-081419AMIST-364645798",
"ID-149214751-070931",
"ID-627687926-083627",
"ID-790095198-092542",
"ID-852030110-100723",
"ID-0610-112746pmGMT+05:30-139532053",
"ID-0611-092555PMIST-735221034",
"ID-38913428-091026",
"ID-0609-070015AMIST-654686807",
"ID-580654251-121757",
"ID-0608-040436PMCDT-925539308",
"ID-583171285-095445",
"ID-0608-114914PMIST-752167907",
"ID-648789065-113716",
"ID-0610-021807PMPDT-173972119",
"ID-808715944-073924",
"ID-0609-013332amIST-15840259",
"ID-0607-102434PMEDT-538158474",
"ID-0608-031329PMEDT-607750466",
"ID-931656709-021946",
"ID-91439664-082450",
"ID-0609-025849PMGMT+05:30-849775200",
"ID-769333586-111101",
"ID-0609-040207AMGMT+08:00-131341161",
"ID-568485306-111251",
"ID-444618943-101110",
"ID-0610-125017PMEDT-21032071",
"ID-0610-022327PMEDT-926203621",
"ID-0608-034842PMPDT-209701736",
"ID-992203133-102322",
"ID-0611-074458AMEDT-629917063",
"ID-0610-123822PMPDT-400201528",
"ID-392462964-083426",
"ID-9840300-021711"

]

print (len(users))

# def getOrderOfRounds(dict):
# 	roundLetters = []
# 	for x in xrange(1,6):
# 		for field in dict:
# 			if (field[8] == str(x)):
# 				roundLetters.append(field[6])
# 				break
# 	return roundLetters

newL = []  
for item in users:
	for userRnd in data["M4M_Phase1"]: 
		if (item == userRnd):
			userValue = data["M4M_Phase1"][userRnd]  
			newL.append(   (userRnd , userValue) )
			
			#print(type(userRnd))
	for userRnd in data["M4M_Phase1_2"]:
		if (item == userRnd):
			userValue = data["M4M_Phase1_2"][userRnd]  
			newL.append(   (userRnd , userValue) )

print (len(newL))
#print (newDict)

newDict = dict(newL)

def readTimestamp(timestamp):
	return datetime.datetime.strptime(timestamp, '%m %d %Y_%H %M %S %p') 
	### how we are (if at all) mediating for the fact that time is recorded
	### in the time zone the device is set to. Therefore, we have GMT, EST, CDT, etc.
	### Since we are only recording the time difference we do NOT have to worry about this issue. 
	### 06 04 2020_08 55 12 AM:

def getRoundTime(user,whichRound):
	ts = dict(newL)[user]["timestamps"]
	rnd = dict(newL)[user]
	startTime = ""
	endTime = ""
	total_Dur=""
	#timestamps are keys, events are values
	print(whichRound + "!")
	for key in sorted(ts):

		#if (not startTime == "") and (endTime == "") and (ts[key].endswith("begins\"") or ts[key]=="\"Game Result\""): 
		if (not startTime == "") and (endTime == "") and (ts[key]=="\"Game Result\""): 
			endTime = key
			#print("t")
			print ("Start Time: " + startTime) 
		if ts[key] == "\"round "+whichRound+" begins\"":
			startTime = key
			#print ("End Time: " + endTime) 
	if (not startTime == "") and (not endTime == ""):
		total_Dur = (str(readTimestamp(endTime) - readTimestamp(startTime)))
		#print ("First Rnd to Game Result Duration: " + str(readTimestamp(endTime) - readTimestamp(startTime)))
	

# 	### this is where I will start the duration the users spent on the community board page in each round
# 	### so there is (if collected properly), five duration instances (each one for each round) per user
# 	## so from "reason submit button click" to "comm submit button click" per each round OR after the first round up to "round # result screen"

# 	for key in sorted(ts):
# 		if ts[key] == "\"reason submit button click\"":
# 			startTime = key
# 			break #break here

# 	for key in sorted(ts):
# 		if ts[key] == "\"round 1 result screen\"":
# 			rnd1_result = key
# 		if ts[key] == "\"round 2 result screen\"":
# 			rnd2_result = key
# 		if ts[key] == "\"round 3 result screen\"":
# 			rnd3_result = key
# 		if ts[key] == "\"round 4 result screen\"":
# 			rnd4_result = key
# 		if ts[key] == "\"round 5 result screen\"":
# 			rnd5_result = key


# 	rnd1_d = readTimestamp(rnd1_result) - readTimestamp(startTime) 
# 	rnd2_d = readTimestamp(rnd2_result) - readTimestamp(rnd1_result) 
# 	rnd3_d = readTimestamp(rnd3_result) - readTimestamp(rnd2_result) 
# 	rnd4_d = readTimestamp(rnd4_result) - readTimestamp(rnd3_result) 
# 	rnd5_d = readTimestamp(rnd5_result) - readTimestamp(rnd4_result) 

# # 	# print("Round A Duration: " + str(rnd1_d))
# # 	# print("Round B Duration: " + str(rnd2_d))
# # 	# print("Round C Duration: " + str(rnd3_d))
# # 	# print("Round D Duration: " + str(rnd4_d))
# # 	# print("Round E Duration: " + str(rnd5_d))
# 	rnd1_dur = str(rnd1_d)
# 	rnd2_dur = str(rnd2_d)
# 	rnd3_dur = str(rnd3_d)
# 	rnd4_dur = str(rnd4_d)
# 	rnd5_dur = str(rnd5_d)


 	init_choice = {} 
# 	# comm_choice = {} 
# 	## initialize them as an empty dictionary and then read them when I am done with the loop

# 	#round_L-#_choice/reason : keys
# 	#numbers (specifically #-#) and reasonings in text: values
 	initial_choices = [ ]
 	initial_reasons = [ ]
	
	rnd_Correct = [ ]
	# rnd2_Correct = [ ]
	# rnd3_Correct = [ ]
	# rnd4_Correct = [ ]
	# rnd5_Correct = [ ]

	for key in sorted(rnd):	
		mealShown = key[8]  ## this is the number after the letter:  B-5 (the number of that format)????
		letter = key[6] ## this is the letter before the number: B-5 (the letter of that format)????
		reason = rnd[key]


		if (key.endswith("_choice")):
			init_choice[str(mealShown)] = rnd[key][1]
			print ("Round " + mealShown + " Choice: " + reason[1])
			#print ("Round Letter: " + letter)
			initial_choices.append(reason[1])
			
			if (reason[1]=="1"):
				#print ("Round 1 correct: YES" )
				rnd_Correct.append(1)
				#print (rnd_Correct)
			else:
				#print ("incorrect")
				rnd_Correct.append(0)


		if (key.endswith("_reason")):
			print ("Round " + mealShown + " Reason: " + reason) 	
			initial_reasons.append(reason)
	print (rnd_Correct)		

	
	return { #"total duration": total_Dur, "round 1 duration": rnd1_dur, "round 2 duration": rnd2_dur, "round 3 duration": rnd3_dur, "round 4 duration": rnd4_dur, "round 5 duration": rnd5_dur, 
			"Turk_choices": initial_choices,
			"Turk_reasons": initial_reasons,
			"Rnd_Correctness": rnd_Correct, 
			}

def firstLetter(ts):
	
	for t in sorted(ts):
		if ( ts[t].startswith("\"round ") and ts[t].endswith("begins\"")  ) : ## believe this is getting the B, D, A, E, C letters under "timestamps"
			return ts[t][7]
	print("didnt find a letter!")
	exit(1)

for user, userData in newL: 
	try:
		print ("Monster Choice: " + newDict[user]["assigned_monster_num"])
		newDict[user]["results"] = getRoundTime(user,firstLetter(newDict[user]["timestamps"])) 
		print ("")
	except Exception as ex:
	    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
	    message = template.format(type(ex).__name__, ex.args)
	    print message




# for ts in newDict[user]["assigned_monster_num"]: 
# 	#print (user)	
# 	try:
# 		#print ("Monster Choice: " + data["M4M_Phase2_AMT"][user]["monster choice"])
# 		#ts = data["M4M_Phase2_AMT"][user]["timestamps"]
# 		data["M4M_Phase2_AMT"][user]["results"] = getRoundTime(user,ts[6]) 
# 		## getRoundTime's function second argument is WHATEVER STRING (A, B, C, D, E) appears first, 
# 		print ("")
# 	except Exception as e:
# 		print (e)
# 		print ("")

# with open('m4m_AMT.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["userID","Monster_Number","First_Rnd_to_Game_Result_Duration","Community_Board_Freq_Clicks_Array","CB_Clicks1",
#     	"CB_Clicks2","CB_Clicks3","CB_Clicks4","CB_Clicks5","Rnd1_Duration","Rnd2_Duration","Rnd3_Duration","Rnd4_Duration","Rnd5_Duration",
#     	"Init_Choice1","Init_Reason1","Community_Choice1","Community_Reason1",
#     	"Init_Choice2","Init_Reason2","Community_Choice2","Community_Reason2",
#     	"Init_Choice3","Init_Reason3","Community_Choice3","Community_Reason3",
#     	"Init_Choice4","Init_Reason4","Community_Choice4","Community_Reason4",
#     	"Init_Choice5","Init_Reason5","Community_Choice5","Community_Reason5",
#     	"Rnd1_Answer_Change","Rnd2_Answer_Change","Rnd3_Answer_Change","Rnd4_Answer_Change","Rnd5_Answer_Change",
#     	"Rnd1_preCB_Correct", "Rnd1_postCB_Correct","Rnd5_preCB_Correct", "Rnd5_postCB_Correct"])
#     for row in data["M4M_Phase2_AMT"]:
#     	try:
#     		writer.writerow([ row, data["M4M_Phase2_AMT"][row]["monster choice"],data["M4M_Phase2_AMT"][row]["results"]["total duration"],data["M4M_Phase2_AMT"][row]["results"]["frequency clicks all"],
    		
    		
#     		## community board clicks to see "engagement" in order of rounds
#     		data["M4M_Phase2_AMT"][row]["results"]["community 1 clicks"],data["M4M_Phase2_AMT"][row]["results"]["community 2 clicks"],data["M4M_Phase2_AMT"][row]["results"]["community 3 clicks"],
#     		data["M4M_Phase2_AMT"][row]["results"]["community 4 clicks"],data["M4M_Phase2_AMT"][row]["results"]["community 5 clicks"],

#     		## durations in order of rounds 
#     		data["M4M_Phase2_AMT"][row]["results"]["round 1 duration"],data["M4M_Phase2_AMT"][row]["results"]["round 2 duration"],data["M4M_Phase2_AMT"][row]["results"]["round 3 duration"],
#     		data["M4M_Phase2_AMT"][row]["results"]["round 4 duration"],data["M4M_Phase2_AMT"][row]["results"]["round 5 duration"],
    		
#     		#round 1 -- choices and reasons
#     		data["M4M_Phase2_AMT"][row]["results"]["initial choices"][0],data["M4M_Phase2_AMT"][row]["results"]["initial reasons"][0],
#     		data["M4M_Phase2_AMT"][row]["results"]["comm choices"][0],data["M4M_Phase2_AMT"][row]["results"]["comm reasons"][0],

#     		#round 2 -- choices and reasons
#     		data["M4M_Phase2_AMT"][row]["results"]["initial choices"][1],data["M4M_Phase2_AMT"][row]["results"]["initial reasons"][1],
#     		data["M4M_Phase2_AMT"][row]["results"]["comm choices"][1],data["M4M_Phase2_AMT"][row]["results"]["comm reasons"][1],

#     		#round 3 -- choices and reasons
#     		data["M4M_Phase2_AMT"][row]["results"]["initial choices"][2],data["M4M_Phase2_AMT"][row]["results"]["initial reasons"][2],
#     		data["M4M_Phase2_AMT"][row]["results"]["comm choices"][2],data["M4M_Phase2_AMT"][row]["results"]["comm reasons"][2],

#     		#round 4 -- choices and reasons
#     		data["M4M_Phase2_AMT"][row]["results"]["initial choices"][3],data["M4M_Phase2_AMT"][row]["results"]["initial reasons"][3],
#     		data["M4M_Phase2_AMT"][row]["results"]["comm choices"][3],data["M4M_Phase2_AMT"][row]["results"]["comm reasons"][3],

#     		#round 5 -- choices and reasons
#     		data["M4M_Phase2_AMT"][row]["results"]["initial choices"][4],data["M4M_Phase2_AMT"][row]["results"]["initial reasons"][4],
#     		data["M4M_Phase2_AMT"][row]["results"]["comm choices"][4],data["M4M_Phase2_AMT"][row]["results"]["comm reasons"][4],

#     		data["M4M_Phase2_AMT"][row]["results"]["answer change"][0],data["M4M_Phase2_AMT"][row]["results"]["answer change"][1], data["M4M_Phase2_AMT"][row]["results"]["answer change"][2], 
#     		data["M4M_Phase2_AMT"][row]["results"]["answer change"][3], data["M4M_Phase2_AMT"][row]["results"]["answer change"][4],

#     		#initial choices in Round 1 
#     		data["M4M_Phase2_AMT"][row]["results"]["Rnd1_preCB_Correct"][0], 
#     		#initial choices in Round 5
# 			data["M4M_Phase2_AMT"][row]["results"]["Rnd1_postCB_Correct"][0],
#     		#post CB choices in Round 1
# 			data["M4M_Phase2_AMT"][row]["results"]["Rnd5_preCB_Correct"][4],
#     		#post CB choices in Round 5
# 			data["M4M_Phase2_AMT"][row]["results"]["Rnd5_postCB_Correct"][4]
#     			])
#     	except Exception as e:
#     		print (e)



























