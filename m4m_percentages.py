import json
import datetime
import csv

with open("meal4monsters-export_2020_06_24.json", "r") as read_file:
    data = json.load(read_file)

class RoundInfo:
    def __init__(self, monster_num, round_num):
        self.monster_num = monster_num
        self.round_num = round_num 
        self.choices = [0,0,0,0]
        self.total = 0

class Monster:
    def __init__(self, monster_num):
        self.rounds = [RoundInfo(monster_num, r) for r in [1,2,3,4,5]]
  
monster_list = [Monster(monster_num) for monster_num in [1,2,3,4]]

def process(userData):
  try:
    mn = int(userData["assigned_monster_num"])
  except Exception as e:
    return 
  for round_num in [1,2,3,4,5]:
    for key in userData:
      if (key.endswith(str(round_num)+"_choice")):
        monster_list[(mn-1)].rounds[round_num-1].total += 1
        monster_list[(mn-1)].rounds[round_num-1].choices[int(userData[key][1])-1] += 1
 
for user in data["M4M_Phase1"]: 
    process(data["M4M_Phase1"][user])
 
for user in data["M4M_Phase1_2"]: 
    process(data["M4M_Phase1_2"][user])

for m in monster_list:
  for r in m.rounds:
    print "Monster Num = " + str(r.monster_num) + " - Round = " + str(r.round_num)
    for c in r.choices:
      print((str(c) + " ("+ str(float(c)/r.total)) + ")")
    print ("total " + str(r.total))
