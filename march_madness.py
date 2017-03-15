import random

class March_Madness(object):
	bracket = { 
		'32': {'east': {}, 'west': {}, 'midwest': {}, 'south': {}},
		'16': {'east': {}, 'west': {}, 'midwest': {}, 'south': {}},
		'8': {'east': {}, 'west': {}, 'midwest': {}, 'south': {}},
		'4': {},
		'2': []
	}
	
	def __init__(self, rounds, random_factor):
		self.rounds = rounds
		self.random_factor = random_factor
		self.divisions = {'east': {}, 'west': {}, 'midwest': {}, 'south': {}}
	
	def add_team(self, team):
		self.divisions[team.division][team.seed] = team
	
	def do_battle(self, team_a, team_b):
		print('{0} VS {1}'.format(str(team_a), str(team_b)))
		first_team_wins = 0
		second_team_wins = 0
					
		if random.randint(0, 1) == 0:
			first = team_a
			second = team_b
		else:
			first = team_a
			second = team_b
		for j in range(0, self.rounds):
			while not first.is_dead() and not second.is_dead():
				if random.randint(0, 500/self.random_factor) == 42:
					print('A DRAGON APPEARS AND LASHES OUT!')
					winner = [first, second][random.randint(0,1)]
					winner.reset_health()
					return winner
				
				second.damage(first.roll_attack(), self.random_factor)
				if second.is_dead():
					first_team_wins += 1
			
				first.damage(second.roll_attack(), self.random_factor)
				if first.is_dead():
					second_team_wins += 1
				
			first.reset_health()
			second.reset_health()
		
		if (first_team_wins > second_team_wins and first.seed > second.seed) or (first_team_wins < second_team_wins and first.seed < second.seed):
			print('UPSET')
		
		return first if first_team_wins > second_team_wins else second
		
	
	def round_of_64(self):
		bracket = {
			1: [1, 16],
			2: [8, 9],
			3: [5, 12],
			4: [4, 13],
			5: [6, 11],
			6: [3, 14],
			7: [7, 10],
			8: [2, 15]
		}
		
		for div in self.divisions:
			division = self.divisions[div]
			
			for i in bracket:
				match = bracket[i]
				winner = self.do_battle(division[match[0]], division[match[1]])
				
				self.bracket['32'][div][i] = winner
				
		self.print_output(self.bracket['32'])
	
	def round_of_32(self):
		bracket = {1: [1,2], 2: [3,4], 3: [5,6], 4: [7,8]}
		for div in self.divisions:
			division = self.divisions[div]
			
			for i in [1,2,3,4]:
				match = bracket[i]
				winner = self.do_battle(self.bracket['32'][div][match[0]], self.bracket['32'][div][match[1]])
				
				self.bracket['16'][div][i] = winner
		
		self.print_output(self.bracket['16'])
	
	def sweet_sixteen(self):
		bracket = {1: [1,2], 2: [3,4]}
		
		for div in self.divisions:
			division = self.divisions[div]
			
			for i in [1,2]:
				match = bracket[i]
				winner = self.do_battle(self.bracket['16'][div][match[0]], self.bracket['16'][div][match[1]])
				
				self.bracket['8'][div][i] = winner
		
		self.print_output(self.bracket['8'])
	
	def elite_eight(self):
		for div in self.divisions:
			division = self.divisions[div]
			winner = self.do_battle(self.bracket['8'][div][1], self.bracket['8'][div][2])
			
			self.bracket['4'][div] = winner
		
		self.print_final_four(self.bracket['4'])
	
	def final_four(self):
		self.bracket['2'].append(self.do_battle(self.bracket['4']['east'], self.bracket['4']['west']))
		self.bracket['2'].append(self.do_battle(self.bracket['4']['midwest'], self.bracket['4']['south']))
		
		print('NATIONAL FINALISTS: {0} and {1}'.format(str(self.bracket['2'][0]), str(self.bracket['2'][1])))
	
	def championship(self):
		self.bracket['winner'] = self.do_battle(self.bracket['2'][0], self.bracket['2'][1])
		print('THE TOURNAMENT CHAMPION IS {0}'.format(self.bracket['winner']))
	
	def print_output(self, bracket_results):
		for div in bracket_results:
			print('{0} DIVISION'.format(div.upper()))
			for i in bracket_results[div]:
				print(str(bracket_results[div][i]))
	
	def print_final_four(self, bracket_results):
		print('WESTERN DIVISION CHAMPIONS: {0}'.format(str(bracket_results['west'])))
		print('EASTERN DIVISION CHAMPIONS: {0}'.format(str(bracket_results['east'])))
		print('MIDWESTERN DIVISION CHAMPIONS: {0}'.format(str(bracket_results['midwest'])))
		print('SOUTHERN DIVISION CHAMPIONS: {0}'.format(str(bracket_results['south'])))
