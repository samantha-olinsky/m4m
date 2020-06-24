import json
import datetime
import csv

with open("meal4monsters-export_v1.2.json", "r") as read_file:
    data = json.load(read_file)

#print((data.keys()))

#print((data["M4M_Phase1"].keys()))

#print((data["M4M_Phase1"]["timestamps"]))

def readTimestamp(timestamp):
	return datetime.datetime.strptime(timestamp, '%m %d %Y_%H %M %S %p')

def getRoundTime(user,whichRound):
	ts = data["M4M_Phase1"][user]["timestamps"]
	rnd = data["M4M_Phase1"][user]
	startTime = ""
	endTime = ""	
	#timestamps are keys, events are values
	for key in sorted(ts):
		if (not startTime == "") and endTime == "" and (ts[key].endswith("begins\"") or ts[key]=="\"Game Result\""):
			endTime = key
			print startTime
		if ts[key] == "\"round "+whichRound+" begins\"":
			startTime = key
	if (not startTime == "") and (not endTime == ""):
		print (readTimestamp(endTime) - readTimestamp(startTime))
	#round_L-#_choice/reason : keys
	#numbers (specifically #-#) and reasonings in text: values
	for key in sorted(rnd):
		if (key.endswith("_reason")):
			reason = rnd[key]
			print ("Round # Reason: " + reason) 

for user in data["M4M_Phase1"]: 
	print user
	try:
		print ("Assigned monster num: " + data["M4M_Phase1"][user]["assigned_monster_num"])
		getRoundTime(user,"A")
		print ""
	except Exception as e:
		print (e)
		print ""


def getRoundTime2(user,whichRound):
	ts2 = data["M4M_Phase1_2"][user]["timestamps"]
	rnd2 = data["M4M_Phase1_2"][user]
	startTime2 = ""
	endTime2 = ""
	
	#timestamps are keys, events are values
	for key in sorted(ts2):
		if (not startTime2 == "") and endTime2 == "" and (ts2[key].endswith("begins\"") or ts2[key]=="\"Game Result\""):
			endTime2 = key
			print startTime2
		if ts2[key] == "\"round "+whichRound+" begins\"":
			startTime2 = key
	if (not startTime2 == "") and (not endTime2 == ""):
		print (readTimestamp(endTime2) - readTimestamp(startTime2))
	#round_L-#_choice/reason : keys
	#numbers (specifically #-#) and reasonings in text: values
	for key in sorted(rnd2):
		if (key.endswith("_reason")):
			reason = rnd2[key]
			print ("Round # Reason: " + reason) 


for user in data["M4M_Phase1_2"]: 
	print user
	try:
		print ("Assigned monster num: " + data["M4M_Phase1_2"][user]["assigned_monster_num"])
		getRoundTime2(user,"A")
		print ""
	except Exception as e:
		print (e)
		print ""


# with open('m4m.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["userID", "monster_number", "reasonings"])
#     for row in writer:
#     	print()
