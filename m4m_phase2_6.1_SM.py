import json
import datetime
import csv

with open("meal4monsters-export_v5.1.json", "r") as read_file:
    data = json.load(read_file)  
    ## Note that I took out one data entry from the JSON file bc the one with Korean in it is not ascii and was
    ## throwing errors. So that one Korean entry (userID that includes Korean) will have to added manually.

users = [


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
## below 0815 did not print
"ID-0815-032743AMIST-703379681",

"ID-0816-084851AMEDT-255935211",
"ID-0816-114356AMEDT-489059163",
"ID-0816-114536AMEDT-374674448",

"ID-0817-014501pmCEST-630779850",
"ID-0817-044223PMEDT-815539722",

"ID-0818-100221AMEDT-592049191",
"ID-0818-112940AMEDT-618142101",

"ID-0819-100243amCEST-351690746",
## 0826 does not
"ID-0826-124603PMIST-530874004",

## below 0822-010
"ID-0822-010948AMGMT+05:30-880630879",
"ID-0822-105045AMEDT-341496192"] 

def getOrderOfRounds(dict):
	roundLetters = []
	for x in xrange(1,6):
		for field in dict:
			if (field[8] == str(x)):
				roundLetters.append(field[6])
				break
	return roundLetters

roundInfo = [ ]
for userRnd in data["M4M_Phase2_SM"]: 
	for item in users:
		if (item == userRnd):
			letters = getOrderOfRounds(data["M4M_Phase2_SM"][userRnd])	
			print(userRnd + ", " + ", ".join(letters))
print (roundInfo)