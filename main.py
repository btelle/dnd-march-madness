from march_madness import March_Madness
from team import Team
import csv, argparse

def get_attack_points(ppg, seed):
	min_ppg = 64
	max_ppg = 90.4
	
	unweighted = int(17 * ((float(ppg) - min_ppg) / (max_ppg - min_ppg))) + (17 - seed)
	return round(5 * (unweighted / 17))

def get_defense_points(oppg, seed):
	min_oppg = 55.6
	max_oppg = 78.2
	
	unweighted = int((17 - (17 * ((float(oppg) - min_oppg) / (max_oppg - min_oppg))))) + (17 - seed)
	return round(5 * (unweighted / 17))

parser = argparse.ArgumentParser()
parser.add_argument('--rounds', help='Number of rounds to simulate for each matchup. Must be odd.', default=3, type=int)
parser.add_argument('--randomness', help='Amount of randomness to simulate, 1-5', default=1, type=int)
args = parser.parse_args()

mm = March_Madness(args.rounds, args.randomness)

with open('teams.csv') as csvfile:
	reader = csv.reader(csvfile)
	next(reader, None)
	
	for row in reader:
		team = Team(row[0], row[1], int(row[2]), get_attack_points(row[3], int(row[2])), get_defense_points(row[4], int(row[2])))
		mm.add_team(team)

print('##########################')
print('# ROUND OF 64')
print('##########################')
mm.round_of_64()
raw_input('Press Enter to continue...')

print('\n##########################')
print('# ROUND OF 32')
print('##########################')
mm.round_of_32()
raw_input('Press Enter to continue...')

print('\n##########################')
print('# SWEET SIXTEEN')
print('##########################')
mm.sweet_sixteen()
raw_input('Press Enter to continue...')

print('\n##########################')
print('# ELITE EIGHT')
print('##########################')
mm.elite_eight()
raw_input('Press Enter to continue...')

print('\n##########################')
print('# FINAL FOUR')
print('##########################')
mm.final_four()
raw_input('Press Enter to continue...')

print('\n##########################')
print('# CHAMPIONSHIP')
print('##########################')
mm.championship()
