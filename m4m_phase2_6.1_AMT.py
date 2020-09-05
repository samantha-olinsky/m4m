import json
import datetime
import csv

with open("meal4monsters-export_v5.1.json", "r") as read_file:
    data = json.load(read_file)  

## a total of 34 LEU
users = [ ## two entries are missing from the output
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

"ID-0818-085456PMEDT-127206547",
## below 0812 is missing
"ID-0812-125410AMBRT-93573122",

"ID-0830-054520PMCDT-2898864",
"ID-0830-103515pmGMT+05:30-620306760",
"ID-0830-084718PMIST-679108612",
"ID-0830-043845pmCEST-88243611",
"ID-0830-023422PMCDT-247099562"
]


def getOrderOfRounds(dict):
	roundLetters = []
	for x in xrange(1,6):
		for field in dict:
			if (field[8] == str(x)):
				roundLetters.append(field[6])
				break
	return roundLetters

roundInfo = [ ]
for userRnd in data["M4M_Phase2_AMT"]: 
	for item in users:
		if (item == userRnd):
			letters = getOrderOfRounds(data["M4M_Phase2_AMT"][userRnd])	
			print(userRnd + ", " + ", ".join(letters))
print (roundInfo)


# def readTimestamp(timestamp):
# 	return datetime.datetime.strptime(timestamp, '%m %d %Y_%H %M %S %p') 
# 	### how we are (if at all) mediating for the fact that time is recorded
# 	### in the time zone the device is set to. Therefore, we have GMT, EST, CDT, etc.
# 	### Since we are only recording the time difference we do NOT have to worry about this issue. 

# def getRoundTime(user,whichRound):
# 	ts = data["M4M_Phase2_AMT"][user]["timestamps"]
# 	rnd = data["M4M_Phase2_AMT"][user]
# 	startTime = ""
# 	endTime = ""
# 	total_Dur=""
# 	#timestamps are keys, events are values
# 	for key in sorted(ts):
# 		#if (not startTime == "") and (endTime == "") and (ts[key].endswith("begins\"") or ts[key]=="\"Game Result\""): 
# 		if (not startTime == "") and (endTime == "") and (ts[key]=="\"Game Result\""): 
# 			endTime = key
# 			#print ("Start Time: " + startTime) 
# 		if ts[key] == "\"round "+whichRound+" begins\"":
# 			startTime = key
# 			#print ("End Time: " + endTime) 
# 	if (not startTime == "") and (not endTime == ""):
# 		total_Dur = (str(readTimestamp(endTime) - readTimestamp(startTime)))
# 		#print ("First Rnd to Game Result Duration: " + str(readTimestamp(endTime) - readTimestamp(startTime)))

	
# 	return {"total duration": total_Dur, "frequency clicks all": freq_clicks_array, "community 1 clicks": cb_1_clicks, "community 2 clicks": cb_2_clicks,
# 			"community 3 clicks": cb_3_clicks, "community 4 clicks": cb_4_clicks, "community 5 clicks": cb_5_clicks, "round 1 duration": rnd1_dur, 
# 			"round 2 duration": rnd2_dur, "round 3 duration": rnd3_dur, "round 4 duration": rnd4_dur, "round 5 duration": rnd5_dur, "initial choices": initial_choices,
# 			"initial reasons": initial_reasons, "comm choices": community_choices, "comm reasons": community_reasons, "answer change": answer_changes,
# 			"Rnd1_preCB_Correct": rnd1_preCB_Correct, 
# 			"Rnd1_postCB_Correct": rnd1_postCB_Correct,
# 			"Rnd5_preCB_Correct": rnd5_preCB_Correct, 
# 			"Rnd5_postCB_Correct": rnd5_postCB_Correct 
# 			}
#  ##calling the function firstLetter
# def firstLetter(ts):
# 	for t in sorted(ts):
# 		if ( ts[t].startswith("\"round ") and ts[t].endswith("begins\"")  ) : 
# 			return ts[t][6]

# for user in data["M4M_Phase2_AMT"]: 
# 	#print (user)

# 	try:
# 		print ("Monster Choice: " + data["M4M_Phase2_AMT"][user]["monster choice"])
# 		data["M4M_Phase2_AMT"][user]["results"] = getRoundTime(user,firstLetter(data["M4M_Phase2_AMT"][user]["timestamps"])) 
# 		print ("")
# 	except Exception as e:
# 		print (e)
# 		print ("")



# with open('m4m_AMT_rnd_order.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["userID","Monster_Number", "Rnd1_Letter","Rnd2_Letter","Rnd3_Letter","Rnd4_Letter","Rnd5_Letter",
#     	])
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

