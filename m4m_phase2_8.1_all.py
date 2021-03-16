import json
import datetime
import csv

with open("meal4monsters-export_v5.1.json", "r") as read_file:
	data = json.load(read_file)

# initializing the variable 'users' with the value of a list of user IDs
users = [ 

"ID-0812-125410AMBRT-93573122",

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

# definining a function 'getOrderOfRounds' being passed the argument 'dict'
def getOrderOfRounds(dict):
	roundLetters = []		# creating an empty list
	for x in xrange(1,6):   # for loop: for each value 'x' from 1 through 6...
		for field in dict:		# for each value 'field' in the 'dict' to be passed into the fn when called...
			if (field[8] == str(x)):   # if the 9th value of the list 'field' is equal to the string 'x' (from above),
				roundLetters.append(field[6])  # add the 7th value of the list 'field' to the 'roundLetters' list (from above)
				break		# break the for loop, so continue iterating the outer for loop.
	return roundLetters     # when the outer for loop has gone through every 'x' value, the function is complete
							## and the list 'roundLetters' is returned.

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
print (roundInfoSM)









