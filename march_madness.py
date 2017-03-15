import random

class March_Madness(object):
	bracket = { 
		'32': {'east': {}, 'west': {}, 'midwest': {}, 'south': {}},
		'16': {'east': {}, 'west': {}, 'midwest': {}, 'south': {}},
		'8': {'east': {}, 'west': {}, 'midwest': {}, 'south': {}},
		'4': {},
		'2': []
	}
	
	def __init__(self, rounds):
		self.rounds = rounds
		self.divisions = {'east': {}, 'west': {}, 'midwest': {}, 'south': {}}
	
	def add_team(self, team):
		self.divisions[team.division][team.seed] = team
	
	def do_battle(self, team_a, team_b):
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
				second.damage(first.roll_attack())
				if second.is_dead():
					first_team_wins += 1
			
				first.damage(second.roll_attack())
				if first.is_dead():
					second_team_wins += 1
				print('first health: {0}, second health: {1}'.format(first.hp, second.hp))
			first.reset_health()
			second.reset_health()
		
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
				
		print(self.bracket['32'])
	
	def round_of_32(self):
		bracket = {1: [1,2], 2: [3,4], 3: [5,6], 4: [7,8]}
		for div in self.divisions:
			division = self.divisions[div]
			
			for i in [1,2,3,4]:
				match = bracket[i]
				winner = self.do_battle(self.bracket['32'][div][match[0]], self.bracket['32'][div][match[1]])
				
				self.bracket['16'][div][i] = winner
		
		print(self.bracket['16'])
	
	def sweet_sixteen(self):
		bracket = {1: [1,2], 2: [3,4]}
		
		for div in self.divisions:
			division = self.divisions[div]
			
			for i in [1,2]:
				match = bracket[i]
				winner = self.do_battle(self.bracket['16'][div][match[0]], self.bracket['16'][div][match[1]])
				
				self.bracket['8'][div][i] = winner
		
		print(self.bracket['8'])
	
	def elite_eight(self):
		for div in self.divisions:
			division = self.divisions[div]
			winner = self.do_battle(self.bracket['8'][div][1], self.bracket['8'][div][2])
			
			self.bracket['4'][div] = winner
		
		print(self.bracket['4'])
	
	def final_four(self):
		self.bracket['2'].append(self.do_battle(self.bracket['4']['east'], self.bracket['4']['west']))
		self.bracket['2'].append(self.do_battle(self.bracket['4']['midwest'], self.bracket['4']['south']))
		
		print(self.bracket['2'])
	
	def championship(self):
		self.bracket['winner'] = self.do_battle(self.bracket['2'][0], self.bracket['2'][1])
		print(self.bracket['winner'])
