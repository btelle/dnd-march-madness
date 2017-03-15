import random

class Team():
	def __init__(self, name, division, seed, ap, dp):
		self.name = name
		self.division = division.lower()
		self.seed = seed
		self.hp = 100
		self.attack_points = ap
		self.defense_points = dp
	
	def roll_attack(self, d=20):
		roll = random.randint(1, d)
		print('Rolled {0}'.format(roll))
		return roll + self.attack_points
	
	def damage(self, damage_amount):
		if random.randint(0, 10) < 8:
			self.hp = self.hp - max(damage_amount - self.defense_points, 0)
		
	def is_dead(self):
		return self.hp <= 0
	
	def reset_health(self):
		self.hp = 100
	
	def __repr__(self):
		return '<{0}|{1}|{2}>'.format(self.name, self.division, self.seed)
