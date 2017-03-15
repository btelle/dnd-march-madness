from march_madness import March_Madness
from team import Team
import csv

def get_attack_points(ppg):
	min_ppg = 64
	max_ppg = 90.4
	
	return int(10 * ((float(ppg) - min_ppg) / (max_ppg - min_ppg)))

def get_defense_points(oppg):
	min_oppg = 55.6
	max_oppg = 78.2
	
	return int(10 * ((float(oppg) - min_oppg) / (max_oppg - min_oppg)))

mm = March_Madness(3)

with open('teams.csv') as csvfile:
	reader = csv.reader(csvfile)
	next(reader, None)
	
	for row in reader:
		team = Team(row[0], row[1], int(row[2]), get_attack_points(row[3]), get_defense_points(row[4]))
		print(team.attack_points)
		mm.add_team(team)

mm.round_of_64()
mm.round_of_32()
mm.sweet_sixteen()
mm.elite_eight()
mm.final_four()
mm.championship()
